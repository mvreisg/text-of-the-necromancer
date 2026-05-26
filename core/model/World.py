from core.graphics.Viewport import Viewport
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Area import Area


class World:
    def __init__(self) -> None:
        self.areas: dict[str, Area] = {}

    def tick(self, keyboard: Keyboard, viewport: Viewport, delta: float) -> None:
        for area in self.areas.values():
            area.tick(keyboard, viewport, delta)

    def render(self, viewport: Viewport) -> None:
        for area in self.areas.values():
            area.render(viewport)

    def create_area(self, name: str, x: int, y: int) -> None:
        self.areas[name] = Area(x, y)

    def get_area(self, name: str) -> Area:
        return self.areas[name]
