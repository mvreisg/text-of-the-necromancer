import tcod


class Cell:
    def __init__(self, x: int, y: int, char: str, need_redraw: bool) -> None:
        self.x = x
        self.y = y
        self.char = char
        self.color = (
            int(255 * 0.7),
            int(255 * 0.7),
            int(255 * 0.7),
        )
        self.need_redraw = need_redraw

    def tick(self) -> None:
        pass

    def render(self, console: tcod.console.Console) -> None:
        if self.need_redraw:
            console.print(self.x, self.y, self.char, fg=self.color)
            self.need_redraw = False
