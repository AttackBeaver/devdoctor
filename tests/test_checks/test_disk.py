from devdoctor.checks.disk import DiskCheck

def test_disk_check_success(mocker):
    mocker.patch("shutil.disk_usage", return_value=mocker.Mock(free=10*1024**3))
    check = DiskCheck(".", min_gb=5)
    success, message = check.run()
    assert success is True
    assert "10.00GB free" in message

def test_disk_check_low_space(mocker):
    mocker.patch("shutil.disk_usage", return_value=mocker.Mock(free=1*1024**3))
    check = DiskCheck(".", min_gb=5)
    success, message = check.run()
    assert success is False
    assert "Low disk space" in message
