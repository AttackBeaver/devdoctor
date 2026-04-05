import psutil
from .base import Check
from ..fixers.kill_port import kill_process_on_port

class PortsCheck(Check):
    def __init__(self, port: int, description: str = ""):
        super().__init__(
            name=f"Port: {port}",
            description=f"Check if port {port} ({description}) is free"
        )
        self.port = port

    def run(self) -> tuple[bool, str]:
        for conn in psutil.net_connections():
            if conn.laddr.port == self.port and conn.status == 'LISTEN':
                try:
                    process = psutil.Process(conn.pid)
                    return False, f"Port {self.port} is occupied by '{process.name()}' (PID: {conn.pid})"
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    return False, f"Port {self.port} is occupied (PID: {conn.pid})"
        return True, f"Port {self.port} is free"

    def fix(self) -> bool:
        return kill_process_on_port(self.port)
