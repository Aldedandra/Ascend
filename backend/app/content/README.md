# Ascend Content Package

The backend imports `ACHIEVEMENTS` and `MODULES` from this package exactly as it did from the former `content.py` module.

## Structure

- `achievements.py` — achievement definitions
- `modules.py` — module metadata and lesson assembly
- `module0/lessonXX.py` — one lesson per file
- `shared/` — reserved for genuinely reusable curriculum helpers

## Adding the next Module 0 lesson

1. Create `module0/lesson05.py` exporting `LESSON`.
2. Import it in `module0/__init__.py`.
3. Add it to the `LESSONS` list.
4. Rebuild the backend and verify `/api/modules` and `/api/lessons/0-5`.

Do not re-create `backend/app/content.py`; Python should load this package instead.
