import os
from pathlib import Path

def ensure_directories(dirs: list[str]) -> bool:
    success = True
    for d in dirs:
        try:
            Path(d).mkdir(parents=True, exist_ok=True)
        except Exception:
            success = False
    return success
