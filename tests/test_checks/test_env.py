from devdoctor.checks.env import EnvCheck

def test_env_check_missing_file(tmp_path):
    env_path = tmp_path / ".env"
    check = EnvCheck(str(env_path), ["VAR1"])
    success, message = check.run()
    assert success is False
    assert "missing" in message

def test_env_check_missing_vars(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("VAR1=val1")
    check = EnvCheck(str(env_path), ["VAR1", "VAR2"])
    success, message = check.run()
    assert success is False
    assert "Missing variables: VAR2" in message
