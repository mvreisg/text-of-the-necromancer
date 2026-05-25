import tcod
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Character import Character
from core.model.Cell import Cell


class Area:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.cells: list[Cell] = []
        self.characters: list[Character] = []

    def tick(self, keyboard: Keyboard) -> None:
        for cell in self.cells:
            cell.tick(keyboard)

        for character in self.characters:
            character.tick(keyboard)

    def render(self, console: tcod.console.Console) -> None:
        for cell in self.cells:
            cell.render(console)

        for character in self.characters:
            character.render(console)

    def create_cell(self, x: int, y: int, character: str) -> None:
        cell = Cell(x, y, character)
        self.cells.append(cell)
