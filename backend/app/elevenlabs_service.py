import os
from typing import Any

import httpx
from fastapi import HTTPException

ELEVENLABS_BASE_URL = "https://api.elevenlabs.io"
DEFAULT_MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_flash_v2_5")


def _api_key() -> str:
    key = os.getenv("ELEVENLABS_API_KEY", "").strip()
    if not key:
        raise HTTPException(status_code=503, detail="ElevenLabs is not configured on the Ascend backend.")
    return key


def _headers() -> dict[str, str]:
    return {"xi-api-key": _api_key(), "Content-Type": "application/json"}


def _upstream_error(response: httpx.Response) -> HTTPException:
    try:
        payload = response.json()
        detail = payload.get("detail", payload)
        if isinstance(detail, dict):
            detail = detail.get("message") or str(detail)
    except Exception:
        detail = response.text or "ElevenLabs request failed."
    return HTTPException(status_code=502, detail=f"ElevenLabs: {detail}")


async def list_voices() -> list[dict[str, Any]]:
    async with httpx.AsyncClient(timeout=20.0) as client:
        response = await client.get(
            f"{ELEVENLABS_BASE_URL}/v2/voices",
            headers={"xi-api-key": _api_key()},
            params={"page_size": 100, "sort": "name", "sort_direction": "asc"},
        )
    if not response.is_success:
        raise _upstream_error(response)
    voices = response.json().get("voices", [])
    return [
        {
            "voice_id": voice.get("voice_id"),
            "name": voice.get("name"),
            "category": voice.get("category"),
            "description": voice.get("description"),
            "labels": voice.get("labels") or {},
            "preview_url": voice.get("preview_url"),
        }
        for voice in voices
    ]


async def create_preview(voice_id: str, text: str, model_id: str | None = None) -> tuple[bytes, dict[str, str]]:
    model = (model_id or DEFAULT_MODEL_ID).strip()
    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{ELEVENLABS_BASE_URL}/v1/text-to-speech/{voice_id}",
            params={"output_format": "mp3_44100_128"},
            headers=_headers(),
            json={
                "text": text,
                "model_id": model,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "style": 0.0,
                    "use_speaker_boost": True,
                    "speed": 0.92,
                },
            },
        )
    if not response.is_success:
        raise _upstream_error(response)
    metadata = {
        "X-Ascend-ElevenLabs-Model": model,
        "X-Ascend-Character-Cost": response.headers.get("character-cost", "unknown"),
        "X-Ascend-Request-Id": response.headers.get("request-id", ""),
    }
    return response.content, metadata


from pathlib import Path
import hashlib
import json

AUDIO_CACHE_ROOT = Path(os.getenv("ASCEND_AUDIO_CACHE_PATH", "/data/audio"))
ASCEND_NARRATORS = {
    "bella": {
        "voice_id": "hpp4J3VqNfWAUOO0d1Us",
        "name": "Bella",
        "description": "Clear & Professional",
    },
    "brian": {
        "voice_id": "nPczCjzI2devNBz1zQrb",
        "name": "Brian",
        "description": "Deep & Calm",
    },
}


def narrator_catalog() -> list[dict[str, str]]:
    return [
        {"id": narrator_id, **narrator}
        for narrator_id, narrator in ASCEND_NARRATORS.items()
    ]


def _narrator(narrator_id: str) -> dict[str, str]:
    narrator = ASCEND_NARRATORS.get(narrator_id.lower())
    if not narrator:
        raise HTTPException(status_code=400, detail="Unknown Ascend narrator.")
    return narrator


def _cache_paths(lesson_id: str, narrator_id: str) -> tuple[Path, Path]:
    safe_lesson = "".join(ch for ch in lesson_id if ch.isalnum() or ch in "-_")
    safe_voice = "".join(ch for ch in narrator_id.lower() if ch.isalnum() or ch in "-_")
    directory = AUDIO_CACHE_ROOT / safe_lesson
    return directory / f"{safe_voice}.mp3", directory / f"{safe_voice}.json"


def cached_lesson_audio(lesson_id: str, narrator_id: str) -> tuple[Path, dict[str, Any]] | None:
    audio_path, metadata_path = _cache_paths(lesson_id, narrator_id)
    if not audio_path.exists() or not metadata_path.exists():
        return None
    try:
        metadata = json.loads(metadata_path.read_text())
    except Exception:
        metadata = {}
    return audio_path, metadata


async def prepare_lesson_audio(
    lesson_id: str,
    narrator_id: str,
    text: str,
    title: str,
) -> dict[str, Any]:
    narrator = _narrator(narrator_id)
    audio_path, metadata_path = _cache_paths(lesson_id, narrator_id)
    text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()

    existing = cached_lesson_audio(lesson_id, narrator_id)
    if existing:
        _, metadata = existing
        if metadata.get("text_hash") == text_hash:
            return {**metadata, "cached": True}

    model = DEFAULT_MODEL_ID
    async with httpx.AsyncClient(timeout=180.0) as client:
        response = await client.post(
            f"{ELEVENLABS_BASE_URL}/v1/text-to-speech/{narrator['voice_id']}",
            params={"output_format": "mp3_44100_128"},
            headers=_headers(),
            json={
                "text": text,
                "model_id": model,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "style": 0.0,
                    "use_speaker_boost": True,
                    "speed": 0.92,
                },
            },
        )

    if not response.is_success:
        raise _upstream_error(response)

    audio_path.parent.mkdir(parents=True, exist_ok=True)
    audio_path.write_bytes(response.content)

    metadata = {
        "lesson_id": lesson_id,
        "title": title,
        "narrator_id": narrator_id,
        "narrator_name": narrator["name"],
        "model_id": model,
        "text_hash": text_hash,
        "character_cost": response.headers.get("character-cost", "unknown"),
        "bytes": len(response.content),
    }
    metadata_path.write_text(json.dumps(metadata, indent=2))
    return {**metadata, "cached": False}
