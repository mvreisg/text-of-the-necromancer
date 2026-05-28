from core.controllers.Player import Player
from core.infrastructure.graphics.Viewport import Viewport
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Cell import Cell


class Character:
    def __init__(
        self, id: str, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.character = character
        self.color = color

    def tick(
        self,
        keyboard: Keyboard,
        viewport: Viewport,
        cells: list[Cell],
        delta: float,
        player: Player,
    ) -> None:
        dx = player.dx
        dy = player.dy
        can_move = self.try_move(dx, dy, cells)
        if can_move:
            self.move(dx, dy)
            viewport.set_position(
                self.x - int(viewport.width / 2),
                self.y - int(viewport.height / 2),
            )
            viewport.translate(dx, dy)

    def render(self, viewport: Viewport) -> None:
        if viewport.is_inside(self.x, self.y):
            viewport.set(self.x, self.y, self.character, self.color)

    def try_move(self, dx: int, dy: int, cells: list[Cell]) -> bool:
        desired_x = self.x + dx
        desired_y = self.y + dy
        for cell in cells:
            if cell.x == desired_x and cell.y == desired_y:
                return True
        return False

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        self.need_redraw = True
