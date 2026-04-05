from devdoctor.checks.tools import ToolCheck

def test_tool_check_success(mocker):
    mocker.patch("devdoctor.checks.tools.get_tool_version", return_value="git version 2.34.1")
    check = ToolCheck("git")
    success, message = check.run()
    assert success is True
    assert "git version 2.34.1" in message

def test_tool_check_fail(mocker):
    mocker.patch("devdoctor.utils.system.get_tool_version", return_value=None)
    check = ToolCheck("nonexistent_tool")
    success, message = check.run()
    assert success is False
    assert "not installed" in message
