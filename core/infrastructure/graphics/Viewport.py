from core.infrastructure.graphics.viewport.ViewportUnit import ViewportUnit


class Viewport:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.units: list[list[ViewportUnit]] = []

    def generate(self) -> None:
        for x in range(self.width):
            row: list[ViewportUnit] = []
            for y in range(self.height):
                row.append(ViewportUnit(x, y, "", (0, 0, 0)))
            self.units.append(row)

    def is_inside(self, x: int, y: int) -> bool:
        if (
            x < self.x
            or y < self.y
            or x >= self.x + self.width
            or y >= self.y + self.height
        ):
            return False
        return True

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set(self, x: int, y: int, character: str, color: tuple[int, int, int]) -> None:
        relative_x = abs(self.x - x)
        relative_y = abs(self.y - y)
        unit = self.units[relative_x][relative_y]
        unit.character = character
        unit.color = color
        unit.must_draw = True
        self.units[relative_x][relative_y] = unit

    def get(self, x: int, y: int) -> ViewportUnit:
        relative_x = abs(self.x - x)
        relative_y = abs(self.y - y)
        return self.units[relative_x][relative_y]
