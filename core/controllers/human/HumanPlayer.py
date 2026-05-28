from core.infrastructure.input.keyboard.KeyCode import KeyCode
from core.infrastructure.input.Keyboard import Keyboard
from core.controllers.Player import Player


class HumanPlayer(Player):
    def __init__(self, character_id: str) -> None:
        super().__init__(character_id)

    def tick(self, keyboard: Keyboard, delta: float) -> None:
        self.dx = 0
        self.dy = 0

        w_pressed = keyboard.get_pressed(KeyCode.W)
        s_pressed = keyboard.get_pressed(KeyCode.S)
        a_pressed = keyboard.get_pressed(KeyCode.A)
        d_pressed = keyboard.get_pressed(KeyCode.D)

        lock_movement = w_pressed and s_pressed and a_pressed and d_pressed
        if lock_movement:
            pass
        elif w_pressed and not s_pressed:
            self.dy = -1
        elif s_pressed and not w_pressed:
            self.dy = 1

        if lock_movement:
            pass
        elif a_pressed and not d_pressed:
            self.dx = -1
        elif d_pressed and not a_pressed:
            self.dx = 1
