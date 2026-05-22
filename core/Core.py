import tcod
from pathlib import Path
from core.infrastructure.input.KeyCode import KeyCode
from core.infrastructure.input.Keyboard import Keyboard
from core.model.Character import Character
from core.model.World import World


class Core:
    def __init__(self) -> None:
        self.is_running = True
        self.row = 0
        self.column = 0
        self.keyboard = Keyboard()
        self.world = World(rows=40, columns=40)
        self.character = Character(x=0, y=0, need_redraw=True)

    def run(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        FONT_PATH = BASE_DIR / "assets/fonts/terminal16x16_gs_ro.png"
        tileset = tcod.tileset.load_tilesheet(
            FONT_PATH, 16, 16, tcod.tileset.CHARMAP_CP437
        )

        self.world.generate()
        self.world.add_character(self.character)

        with tcod.context.new(
            columns=self.world.columns,
            rows=self.world.rows,
            tileset=tileset,
            title="Text of The Necromancer",
        ) as context:
            console = tcod.console.Console(
                width=self.world.columns, height=self.world.rows
            )

            console.clear()

            self.world.render(console)

            while self.is_running:
                for event in tcod.event.wait():
                    if isinstance(event, tcod.event.KeyDown):
                        self.keyboard.set_pressed(
                            KeyCode.Q, event.sym == tcod.event.KeySym.Q
                        )
                        self.keyboard.set_pressed(
                            KeyCode.W, event.sym == tcod.event.KeySym.W
                        )
                        self.keyboard.set_pressed(
                            KeyCode.S, event.sym == tcod.event.KeySym.S
                        )
                        self.keyboard.set_pressed(
                            KeyCode.A, event.sym == tcod.event.KeySym.A
                        )
                        self.keyboard.set_pressed(
                            KeyCode.D, event.sym == tcod.event.KeySym.D
                        )

                        if self.keyboard.get_pressed(KeyCode.Q):
                            self.is_running = False
                            break

                        self.world.tick(self.keyboard)
                        self.world.render(console)

                    context.present(console=console, integer_scaling=True)
