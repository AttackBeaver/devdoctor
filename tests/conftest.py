import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_subprocess(mocker):
    return mocker.patch("subprocess.run")

@pytest.fixture
def mock_psutil(mocker):
    return mocker.patch("psutil.disk_usage")
