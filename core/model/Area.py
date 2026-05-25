from core.model.Character import Character
from core.model.Cell import Cell


class Area:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.cells: list[Cell] = []
        self.characters: list[Character] = []
