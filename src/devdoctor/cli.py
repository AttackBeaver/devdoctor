import click
import shutil
from pathlib import Path
from typing import List, Any
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

from .config import load_config, DEFAULT_CONFIG_NAME
from .reporter import Reporter
from .checks import ToolCheck, PortsCheck, DiskCheck, PathCheck, EnvCheck
from .checks.custom import CustomCheck
from .checks.base import Check

@click.group()
@click.version_option()
def main() -> None:
    """DevEnv Doctor: Professional diagnostic tool for your development environment."""
    pass

@main.command()
@click.option('--fix', is_flag=True, help='Try to fix issues automatically.')
@click.option('--verbose', is_flag=True, help='Show detailed debug info.')
@click.option('--quiet', is_flag=True, help='Only show summary.')
@click.option('--ai', is_flag=True, help='Get AI suggestions for failed checks.')
def check(fix: bool, verbose: bool, quiet: bool, ai: bool) -> None:
    """Run environment diagnostics and optionally fix issues."""
    config = load_config()
    reporter = Reporter()
    checks: List[Check] = []
    
    # 1. Tools
    for t in config.get('tools', []):
        checks.append(ToolCheck(t['name'], t.get('min_version')))
        checks.append(PathCheck(t['name']))
    
    # 2. Ports
    for p in config.get('ports', []):
        port_num = p if isinstance(p, int) else p.get('number')
        desc = "" if isinstance(p, int) else p.get('description', '')
        checks.append(PortsCheck(port_num, desc))
        
    # 3. Disk & Dirs
    dirs = config.get('directories_to_create', [])
    for path in config.get('disk_paths', ['.']):
        checks.append(DiskCheck(path, dirs_to_create=dirs))
        
    # 4. Env
    env_vars = config.get('required_env_vars', [])
    for env_file in config.get('env_files', ['.env']):
        checks.append(EnvCheck(env_file, env_vars))

    # 5. Custom
    for cc in config.get('custom_checks', []):
        checks.append(CustomCheck(cc))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("[cyan]Running diagnostics...", total=len(checks))
        
        for c in checks:
            if verbose:
                progress.console.print(f"Checking: [bold]{c.name}[/bold]")
            
            success, message = c.run()
            if not success and fix:
                if c.fix():
                    reporter.add_fix(c.name, True)
                    success, message = c.run() # Re-run after fix
                else:
                    reporter.add_fix(c.name, False)
            
            status = "OK" if success else "FAIL"
            reporter.add_result(c.name, status, message)
            progress.advance(task)

    if not quiet:
        reporter.print_report()
    else:
        failed = [r for r in reporter.results if r["status"] != "OK"]
        click.echo(f"Status: {'FAIL' if failed else 'OK'} ({len(failed)} issues)")

    if ai:
        from .ai_advisor import get_ai_suggestions
        with progress.console.status("[bold yellow]Consulting AI advisor..."):
            advice = get_ai_suggestions(reporter.results)
        progress.console.print(Panel(advice, title="AI Suggestions", border_style="yellow"))

@main.command()
def init() -> None:
    """Initialize .devdoctor.yaml from example template."""
    example = Path(".devdoctor.yaml.example")
    target = Path(DEFAULT_CONFIG_NAME)
    
    if target.exists():
        click.confirm(f"{DEFAULT_CONFIG_NAME} already exists. Overwrite?", abort=True)
    
    if example.exists():
        shutil.copy(example, target)
        click.echo(f"Successfully created {DEFAULT_CONFIG_NAME} from example.")
    else:
        with open(target, 'w', encoding='utf-8') as f:
            f.write("tools:\n  - name: git\n")
        click.echo(f"Created default {DEFAULT_CONFIG_NAME} (example not found).")


if __name__ == "__main__":
    main()
