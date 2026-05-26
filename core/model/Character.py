from core.graphics.Viewport import Viewport
from core.infrastructure.input.KeyCode import KeyCode
from core.infrastructure.input.Keyboard import Keyboard


class Character:
    def __init__(
        self, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        self.x = x
        self.y = y
        self.character = character
        self.color = color

    def tick(self, keyboard: Keyboard, viewport: Viewport, delta: float) -> None:
        horizontal_movement = 0
        vertical_movement = 0

        w_pressed = keyboard.get_pressed(KeyCode.W)
        s_pressed = keyboard.get_pressed(KeyCode.S)
        a_pressed = keyboard.get_pressed(KeyCode.A)
        d_pressed = keyboard.get_pressed(KeyCode.D)

        lock_movement = w_pressed and s_pressed and a_pressed and d_pressed
        if lock_movement:
            pass
        elif w_pressed and not s_pressed:
            vertical_movement = -1
        elif s_pressed and not w_pressed:
            vertical_movement = 1

        if lock_movement:
            pass
        elif a_pressed and not d_pressed:
            horizontal_movement = -1
        elif d_pressed and not a_pressed:
            horizontal_movement = 1

        can_move = self.try_move(horizontal_movement, vertical_movement)
        if can_move:
            self.move(horizontal_movement, vertical_movement)
            viewport.translate(horizontal_movement, vertical_movement)

    def render(self, viewport: Viewport) -> None:
        if viewport.is_inside(self.x, self.y):
            viewport.set(self.x, self.y, self.character, self.color)

    def try_move(self, dx: int, dy: int) -> bool:
        return True

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        self.need_redraw = True
