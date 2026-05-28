from core.controllers.Player import Player
from core.controllers.human.HumanPlayer import HumanPlayer
from core.infrastructure.graphics.Viewport import Viewport
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Area import Area


class World:
    def __init__(self) -> None:
        self.areas: dict[str, Area] = {}
        self.players: list[Player] = []

    def tick(self, keyboard: Keyboard, viewport: Viewport, delta: float) -> None:
        for player in self.players:
            player.tick(keyboard, delta)

        for area in self.areas.values():
            area.tick(keyboard, viewport, delta, self.players)

    def render(self, viewport: Viewport) -> None:
        for area in self.areas.values():
            area.render(viewport)

    def create_area(self, name: str, x: int, y: int) -> None:
        self.areas[name] = Area(x, y)

    def create_player(self, character_id: str) -> None:
        self.players.append(HumanPlayer(character_id))

    def get_area(self, name: str) -> Area:
        return self.areas[name]
