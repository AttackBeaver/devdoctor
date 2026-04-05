import shutil
from .base import Check

class PathCheck(Check):
    def __init__(self, bin_name: str):
        super().__init__(
            name=f"PATH: {bin_name}",
            description=f"Check if {bin_name} is in PATH and executable"
        )
        self.bin_name = bin_name

    def run(self) -> tuple[bool, str]:
        path = shutil.which(self.bin_name)
        if path:
            return True, f"Found at: {path}"
        return False, f"'{self.bin_name}' not found in PATH"

    def fix(self) -> bool:
        return False
