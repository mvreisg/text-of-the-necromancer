from core.controllers.Player import Player
from core.graphics.Viewport import Viewport
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Character import Character
from core.model.Cell import Cell


class Area:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.cells: list[Cell] = []
        self.characters: list[Character] = []

    def tick(
        self,
        keyboard: Keyboard,
        viewport: Viewport,
        delta: float,
        players: list[Player],
    ) -> None:
        for cell in self.cells:
            cell.tick(keyboard, viewport, delta)

        for character in self.characters:
            for player in players:
                if player.character_id == character.id:
                    character.tick(keyboard, viewport, self.cells, delta, player)

    def render(self, viewport: Viewport) -> None:
        for cell in self.cells:
            cell.render(viewport)

        for character in self.characters:
            character.render(viewport)

    def create_cell(
        self, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        cell = Cell(x, y, character, color)
        self.cells.append(cell)

    def create_character(
        self, id: str, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        c = Character(id, x, y, character, color)
        self.characters.append(c)
