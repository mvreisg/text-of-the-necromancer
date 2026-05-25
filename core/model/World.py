import tcod
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Area import Area


class World:
    def __init__(self, rows: int, columns: int) -> None:
        self.areas: list[Area] = []
        self.need_redraw = True

    def tick(self, keyboard: Keyboard) -> None:
        for area in self.areas:
            for cell in area.cells:
                cell.tick()

            for c in area.characters:
                c.tick(keyboard, area)

    def render(self, console: tcod.console.Console) -> None:
        for area in self.areas:
            for cell in area.cells:
                cell.render(console)

            for c in area.characters:
                c.render(console)
