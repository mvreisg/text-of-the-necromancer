import tcod
from core.infrastructure.input.KeyCode import KeyCode
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Area import Area


class Character:
    def __init__(self, x: int, y: int, need_redraw: bool) -> None:
        self.x: int = x
        self.y: int = y
        self.char = "@"
        self.color = (0, 0, 255)
        self.need_redraw = need_redraw

    def tick(self, keyboard: Keyboard, area: Area) -> None:
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

        can_move = self.try_move(horizontal_movement, vertical_movement, area)
        if can_move:
            self.move(horizontal_movement, vertical_movement)

    def render(self, console: tcod.console.Console) -> None:
        if self.need_redraw:
            console.print(self.x, self.y, self.char, fg=self.color)
            self.need_redraw = False

    def try_move(self, dx: int, dy: int, area: Area) -> bool:
        return True

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        self.need_redraw = True
