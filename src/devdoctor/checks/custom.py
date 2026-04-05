import subprocess
from pathlib import Path
from typing import Tuple
from .base import Check

class CustomCheck(Check):
    def __init__(self, config: dict):
        name = config.get("name", "Custom Check")
        super().__init__(name=name, description=config.get("description", ""))
        self.config = config
        self.check_type = config.get("type", "command")

    def run(self) -> Tuple[bool, str]:
        if self.check_type == "command":
            return self._run_command()
        elif self.check_type == "file_exists":
            return self._run_file_exists()
        return False, f"Unknown check type: {self.check_type}"

    def _run_command(self) -> Tuple[bool, str]:
        cmd = self.config.get("command")
        expected = self.config.get("expected_output_contains")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                if not expected or expected in result.stdout:
                    return True, "Command executed successfully"
                return False, f"Output mismatch. Expected: {expected}"
            return False, f"Command failed with exit code {result.returncode}"
        except Exception as e:
            return False, str(e)

    def _run_file_exists(self) -> Tuple[bool, str]:
        path = Path(self.config.get("path", ""))
        should_exist = self.config.get("should_exist", True)
        exists = path.exists()
        if exists == should_exist:
            return True, f"Path {path} {'exists' if exists else 'does not exist'} as expected"
        return False, f"Path {path} {'exists' if exists else 'does not exist'} (unexpected)"

    def fix(self) -> bool:
        fix_cmd = self.config.get("fix_command") or self.config.get("fix")
        if not fix_cmd:
            return False
        try:
            subprocess.run(fix_cmd, shell=True, check=True)
            return True
        except Exception:
            return False
