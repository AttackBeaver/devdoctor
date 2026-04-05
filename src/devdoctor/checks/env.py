from pathlib import Path
from .base import Check
from ..fixers.env_generator import generate_env_if_missing

class EnvCheck(Check):
    def __init__(self, env_path: str, required_vars: list[str]):
        super().__init__(
            name=f"Env: {env_path}",
            description=f"Check if {env_path} exists and contains required variables"
        )
        self.env_path = Path(env_path)
        self.required_vars = required_vars

    def run(self) -> tuple[bool, str]:
        if not self.env_path.exists():
            return False, f"File {self.env_path} is missing"
        
        content = self.env_path.read_text()
        missing = []
        for var in self.required_vars:
            if f"{var}=" not in content:
                missing.append(var)
        
        if missing:
            return False, f"Missing variables: {', '.join(missing)}"
        
        return True, "All required variables present"

    def fix(self) -> bool:
        return generate_env_if_missing(str(self.env_path), self.required_vars)
