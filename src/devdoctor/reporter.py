from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Reporter:
    def __init__(self):
        self.console = Console()
        self.results = []
        self.fixes = []

    def add_result(self, check_name: str, status: str, message: str):
        self.results.append({
            "check": check_name,
            "status": status,
            "message": message
        })

    def add_fix(self, check_name: str, success: bool):
        self.fixes.append({
            "check": check_name,
            "success": success
        })

    def print_report(self):
        table = Table(title="DevEnv Doctor Report")
        table.add_column("Check", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Message")

        for res in self.results:
            color = "green" if res["status"] == "OK" else "red"
            table.add_row(res["check"], f"[{color}]{res['status']}[/{color}]", res["message"])

        self.console.print(table)
        
        if self.fixes:
            fix_table = Table(title="Fixes Applied")
            fix_table.add_column("Check", style="cyan")
            fix_table.add_column("Result", style="bold")
            for fix in self.fixes:
                color = "green" if fix["success"] else "yellow"
                status = "FIXED" if fix["success"] else "FAILED"
                fix_table.add_row(fix["check"], f"[{color}]{status}[/{color}]")
            self.console.print(fix_table)

        failed = [r for r in self.results if r["status"] != "OK"]
        if failed and not self.fixes:
            self.console.print(Panel(f"Found {len(failed)} issues!", style="red"))
        elif not failed:
            self.console.print(Panel("All checks passed!", style="green"))
