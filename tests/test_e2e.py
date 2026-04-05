from click.testing import CliRunner
from devdoctor.cli import main
import os
from pathlib import Path

def test_e2e_flow(tmp_path):
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path):
        # 1. Init
        # Создаем пример файла
        with open(".devdoctor.yaml.example", "w") as f:
            f.write("tools: []\nenv_files: ['.env']\nrequired_env_vars: ['TEST_VAR']")
        
        result = runner.invoke(main, ["init"], input="y\n")
        assert result.exit_code == 0
        assert Path(".devdoctor.yaml").exists()
        
        # 2. Check
        result = runner.invoke(main, ["check"])
        assert "FAIL" in result.output
        
        # 3. Fix
        result = runner.invoke(main, ["check", "--fix"])
        assert "FIXED" in result.output
        assert Path(".env").exists()
        assert "TEST_VAR=" in Path(".env").read_text()
