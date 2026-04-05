import psutil
import click

def kill_process_on_port(port: int) -> bool:
    for conn in psutil.net_connections():
        if conn.laddr.port == port and conn.status == 'LISTEN':
            try:
                process = psutil.Process(conn.pid)
                if click.confirm(f"Kill process '{process.name()}' (PID: {conn.pid}) on port {port}?", default=False):
                    process.terminate()
                    process.wait(timeout=3)
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                return False
    return False
