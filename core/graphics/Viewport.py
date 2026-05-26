from core.graphics.ViewportUnit import ViewportUnit


class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.units: list[list[ViewportUnit]] = []

    def generate(self) -> None:
        for y in range(self.height):
            row: list[ViewportUnit] = []
            for x in range(self.width):
                row.append(ViewportUnit(x, y, "", (0, 0, 0)))
            self.units.append(row)

    def is_inside(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            return False
        return True

    def translate(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def set(self, x: int, y: int, character: str, color: tuple[int, int, int]) -> None:
        unit = self.units[x][y]
        unit.character = character
        unit.color = color
        unit.is_valid = False
        self.units[x][y] = unit

    def get(self, x: int, y: int) -> ViewportUnit:
        return self.units[x][y]

    def validate(self, x: int, y: int) -> None:
        self.units[x][y].is_valid = True
