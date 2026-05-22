import tcod
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Cell import Cell
from core.model.Character import Character


class World:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.cells: list[list[Cell]] = []
        self.characters: list[Character] = []
        self.need_redraw = True

    def tick(self, keyboard: Keyboard) -> None:
        for r in range(self.rows):
            for c in range(self.columns):
                self.cells[r][c].tick()

        for c in self.characters:
            character_x = c.x
            character_y = c.y
            c.tick(keyboard, 0, self.columns - 1, 0, self.rows - 1)
            if character_x != c.x or character_y != c.y:
                self.cells[character_y][character_x].set_need_redraw_state(True)

    def render(self, console: tcod.console.Console) -> None:
        for r in range(self.rows):
            for c in range(self.columns):
                self.cells[r][c].render(console)

        for c in self.characters:
            c.render(console)

    def generate(self):
        for r in range(self.rows):
            columns: list[Cell] = []
            for c in range(self.columns):
                columns.append(Cell(c, r, "#", True))
            self.cells.append(columns)

    def add_character(self, character: Character) -> None:
        self.characters.append(character)

    def get_cell(self, row: int, column: int) -> Cell:
        return self.cells[row][column]

    def set_need_redraw_state(self, need_redraw: bool) -> None:
        self.need_redraw = need_redraw
