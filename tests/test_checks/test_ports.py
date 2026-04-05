import psutil
from devdoctor.checks.ports import PortsCheck

def test_ports_check_free(mocker):
    mocker.patch("psutil.net_connections", return_value=[])
    check = PortsCheck(9999)
    success, message = check.run()
    assert success is True
    assert "free" in message

def test_ports_check_occupied(mocker):
    mock_conn = mocker.Mock()
    mock_conn.laddr.port = 9999
    mock_conn.status = 'LISTEN'
    mock_conn.pid = 1234
    mocker.patch("psutil.net_connections", return_value=[mock_conn])
    
    mock_proc = mocker.Mock()
    mock_proc.name.return_value = "test_proc"
    mocker.patch("psutil.Process", return_value=mock_proc)
    
    check = PortsCheck(9999)
    success, message = check.run()
    assert success is False
    assert "occupied by 'test_proc'" in message
