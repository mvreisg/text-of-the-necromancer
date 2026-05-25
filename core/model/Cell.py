import tcod

from core.infrastructure.input.Keyboard import Keyboard


class Cell:
    def __init__(self, x: int, y: int, character: str) -> None:
        self.x = x
        self.y = y
        self.character = character
        self.color = (
            int(255 * 0.7),
            int(255 * 0.7),
            int(255 * 0.7),
        )

    def tick(self, keyboard: Keyboard) -> None:
        pass

    def render(self, console: tcod.console.Console) -> None:
        console.print(self.x, self.y, self.character, fg=self.color)
