from core.model.World import World


class Character:
    def __init__(self, x: int, y: int, need_redraw: bool) -> None:
        self.x = x
        self.y = y
        self.char = "@"
        self.color = (0, 0, 255)
        self.need_redraw = need_redraw

    def move(self, world: World, dx: int, dy: int) -> None:
        before_x = self.x
        before_y = self.y

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

        if self.x != before_x or self.y != before_y:
            world.set_redraw_state(before_y, before_x, True)
            self.set_redraw_state(True)

    def set_redraw_state(self, need_redraw: bool) -> None:
        self.need_redraw = need_redraw
