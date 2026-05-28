from core.infrastructure.graphics.Viewport import Viewport
from core.infrastructure.input.Keyboard import Keyboard


class Cell:
    def __init__(
        self, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        self.x = x
        self.y = y
        self.character = character
        self.color = color

    def tick(self, keyboard: Keyboard, viewport: Viewport, delta: float) -> None:
        pass

    def render(self, viewport: Viewport) -> None:
        if viewport.is_inside(self.x, self.y):
            viewport.set(self.x, self.y, self.character, self.color)
