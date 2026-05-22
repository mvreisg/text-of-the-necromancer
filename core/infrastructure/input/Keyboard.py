from core.infrastructure.input.Key import Key
from core.infrastructure.input.KeyCode import KeyCode


class Keyboard:
    def __init__(self) -> None:
        self.keys: dict[KeyCode, Key] = {
            KeyCode.Q: Key(),
            KeyCode.W: Key(),
            KeyCode.S: Key(),
            KeyCode.A: Key(),
            KeyCode.D: Key(),
        }
        pass

    def set_pressed(self, key_code: KeyCode, is_pressed: bool) -> None:
        self.keys[key_code].set_is_pressed(is_pressed)

    def get_pressed(self, key_code: KeyCode) -> bool:
        return self.keys[key_code].is_pressed
