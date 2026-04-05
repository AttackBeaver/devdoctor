import yaml
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG_NAME = ".devdoctor.yaml"

def load_config(path: str | Path | None = None) -> Dict[str, Any]:
    config_path = Path(path or DEFAULT_CONFIG_NAME)
    if not config_path.exists():
        return {}
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f) or {}
    
    # Дефолтные значения для новых ключей
    defaults = {
        "tools": [],
        "ports": [],
        "disk_paths": ["."],
        "directories_to_create": [],
        "env_files": [".env"],
        "required_env_vars": []
    }
    for key, value in defaults.items():
        config.setdefault(key, value)
        
    return config
