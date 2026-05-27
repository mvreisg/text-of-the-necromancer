from core.infrastructure.input.Keyboard import Keyboard


class Player:
    def __init__(self, character_id: str) -> None:
        self.character_id = character_id
        self.dx = 0
        self.dy = 0

    def tick(self, keyboard: Keyboard, delta: float) -> None:
        pass
