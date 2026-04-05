import shutil
from pathlib import Path
from .base import Check
from ..fixers.create_dirs import ensure_directories

class DiskCheck(Check):
    def __init__(self, path: str, min_gb: float = 1.0, dirs_to_create: list[str] = None):
        super().__init__(
            name=f"Disk: {path}",
            description=f"Check free space (min {min_gb}GB) and required directories"
        )
        self.path = path
        self.min_gb = min_gb
        self.dirs_to_create = dirs_to_create or []

    def run(self) -> tuple[bool, str]:
        try:
            usage = shutil.disk_usage(self.path)
            free_gb = usage.free / (1024**3)
            if free_gb < self.min_gb:
                return False, f"Low disk space: {free_gb:.2f}GB free (required {self.min_gb}GB)"
            
            missing = [d for d in self.dirs_to_create if not Path(d).exists()]
            if missing:
                return False, f"Missing directories: {', '.join(missing)}"
                
            return True, f"{free_gb:.2f}GB free, all directories exist"
        except FileNotFoundError:
            return False, f"Path not found: {self.path}"

    def fix(self) -> bool:
        if self.dirs_to_create:
            return ensure_directories(self.dirs_to_create)
        return False
