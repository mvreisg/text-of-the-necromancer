class ViewportUnit:
    def __init__(
        self, x: int, y: int, character: str, color: tuple[int, int, int]
    ) -> None:
        self.x = x
        self.y = y
        self.character = character
        self.color = color
        self.is_valid = False
