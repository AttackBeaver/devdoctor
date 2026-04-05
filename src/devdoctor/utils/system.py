import shutil
import subprocess
import socket
import psutil
from pathlib import Path

def get_tool_version(tool: str) -> str | None:
    try:
        result = subprocess.run(
            [tool, "--version"], 
            capture_output=True, 
            text=True, 
            check=False
        )
        output = result.stdout.strip() or result.stderr.strip()
        # Простой парсинг первой строки (например, "git version 2.34.1")
        return output.split('\n')[0] if output else None
    except FileNotFoundError:
        return None

def is_port_open(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def get_free_disk_space(path: str = ".") -> float:
    usage = psutil.disk_usage(path)
    return usage.free / (1024**3)  # GB

def check_path_for_binary(bin_name: str) -> bool:
    return shutil.which(bin_name) is not None
