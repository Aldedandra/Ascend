#!/bin/zsh
set -euo pipefail

ASCEND="${HOME}/Projects/Ascend"
AUDIO="${HOME}/Projects/Ascend-Audio/lessons"
DEST="${ASCEND}/frontend/public/audio/module0"

mkdir -p "${DEST}"

copy_lesson() {
  local id="$1"
  local slug="$2"
  local src="${AUDIO}/${slug}/${slug}.wav"
  local dst="${DEST}/${id}.wav"

  if [[ ! -f "${src}" ]]; then
    echo "ERROR: Missing ${src}"
    exit 1
  fi

  cp "${src}" "${dst}"
  echo "✓ ${id}  $(du -h "${dst}" | awk '{print $1}')"
}

echo
echo "Installing Module 0 Narrator A Gold Master audio..."
echo

copy_lesson "0-1" "lesson-0-1-how-engineers-think"
copy_lesson "0-2" "lesson-0-2-evidence-before-action"
copy_lesson "0-3" "lesson-0-3-the-internet-is-computers-talking"
copy_lesson "0-4" "lesson-0-4-anatomy-of-a-modern-application"
copy_lesson "0-5" "lesson-0-5-what-devops-actually-connects"
copy_lesson "0-6" "lesson-0-6-reliability-automation-feedback"
copy_lesson "0-7" "lesson-0-7-engineering-foundations-capstone"

echo
echo "Installed:"
ls -lh "${DEST}"/*.wav
echo
echo "Module 0 Gold Master audio is ready for the Ascend frontend build."
