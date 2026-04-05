import yaml
from devdoctor.config import load_config

def test_load_config_empty(tmp_path):
    config_file = tmp_path / ".devdoctor.yaml"
    # Файл не существует
    assert load_config(config_file) == {}

def test_load_config_valid(tmp_path):
    config_file = tmp_path / ".devdoctor.yaml"
    data = {"tools": [{"name": "git"}]}
    with open(config_file, "w") as f:
        yaml.dump(data, f)
    
    loaded = load_config(config_file)
    assert loaded["tools"] == data["tools"]
    assert "ports" in loaded
    assert "disk_paths" in loaded
