from random import Random


class Cell:
    def __init__(self, x: int, y: int, char: str, need_redraw: bool) -> None:
        self.random = Random()
        self.x = x
        self.y = y
        self.char = char
        self.color = (
            int(255 * 0.7),
            int(255 * 0.7),
            int(255 * 0.7),
        )
        self.need_redraw = need_redraw

    def set_redraw_state(self, need_redraw: bool) -> None:
        self.need_redraw = need_redraw
