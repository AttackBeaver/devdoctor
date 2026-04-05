from pathlib import Path

def generate_env_if_missing(env_path: str, required_vars: list[str]) -> bool:
    path = Path(env_path)
    try:
        existing_content = path.read_text() if path.exists() else ""
        new_lines = []
        
        for var in required_vars:
            if f"{var}=" not in existing_content:
                new_lines.append(f"{var}=YOUR_{var}_HERE")
        
        if new_lines:
            with open(path, "a") as f:
                if existing_content and not existing_content.endswith("\n"):
                    f.write("\n")
                f.write("\n".join(new_lines) + "\n")
        return True
    except Exception:
        return False
