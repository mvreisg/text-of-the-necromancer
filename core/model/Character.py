from core.model.World import World


class Character:
    def __init__(
        self,
        x: int,
        y: int
    ) -> None:
        self.x = x
        self.y = y
        self.char = "@"
        self.color = (
            0,
            0,
            255
        )

    def move(
        self,
        world: World, 
        dx: int, 
        dy: int
    ) -> None:
        self.x += dx
        self.y += dy

        if self.x < 0:
            self.x = 0

        if self.y < 0:
            self.y = 0

        if self.x > world.columns - 1:
            self.x = world.columns - 1

        if self.y > world.rows - 1:
            self.y = world.rows - 1            