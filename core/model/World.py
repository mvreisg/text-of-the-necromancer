import tcod
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Area import Area


class World:
    def __init__(self) -> None:
        self.areas: dict[str, Area] = {}

    def tick(self, keyboard: Keyboard) -> None:
        for area in self.areas.values():
            area.tick(keyboard)

    def render(self, console: tcod.console.Console) -> None:
        for area in self.areas.values():
            area.render(console)

    def create_area(self, name: str, x: int, y: int) -> None:
        self.areas[name] = Area(x, y)

    def get_area(self, name: str) -> Area:
        return self.areas[name]
