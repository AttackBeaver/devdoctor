from .base import Check
from ..utils.system import get_tool_version

class ToolCheck(Check):
    def __init__(self, tool_name: str, min_version: str = None):
        super().__init__(
            name=f"Tool: {tool_name}",
            description=f"Check if {tool_name} is installed (min version: {min_version or 'any'})"
        )
        self.tool_name = tool_name
        self.min_version = min_version

    def run(self) -> tuple[bool, str]:
        version = get_tool_version(self.tool_name)
        if not version:
            return False, f"{self.tool_name} is not installed"
        
        # В MVP просто проверяем наличие. Сравнение версий можно добавить позже.
        return True, f"Found: {version}"

    def fix(self) -> bool:
        # Авто-фикс для инструментов обычно требует пакетного менеджера (brew, apt)
        return False
