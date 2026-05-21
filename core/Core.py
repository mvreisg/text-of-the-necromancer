import tcod
from pathlib import Path
from core.model.Character import Character
from core.model.World import World


class Core:
    def __init__(self) -> None:
        self.is_running = True
        self.row = 0
        self.column = 0

    def render(
        self,
        context: tcod.context.Context,
        console: tcod.console.Console,
        world: World,
        character: Character,
    ) -> None:
        for r in range(world.rows):
            for c in range(world.columns):
                cell = world.get_cell(r, c)
                if cell.need_redraw:
                    console.print(cell.x, cell.y, cell.char, fg=cell.color)
                    world.set_redraw_state(r, c, False)

        if character.need_redraw:
            console.print(character.x, character.y, character.char, fg=character.color)
            character.set_redraw_state(False)

        context.present(console=console, keep_aspect=True)

    def run(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        FONT_PATH = BASE_DIR / "assets/fonts/terminal16x16_gs_ro.png"
        tileset = tcod.tileset.load_tilesheet(
            FONT_PATH, 16, 16, tcod.tileset.CHARMAP_CP437
        )

        world = World(rows=40, columns=40)
        world.generate()

        character = Character(x=0, y=0, need_redraw=True)

        with tcod.context.new(
            columns=world.columns,
            rows=world.rows,
            tileset=tileset,
            title="Text of The Necromancer",
        ) as context:
            console = tcod.console.Console(width=world.columns, height=world.rows)

            console.clear()

            self.render(context, console, world, character)

            while self.is_running:
                need_redraw = False
                for event in tcod.event.wait():
                    if isinstance(event, tcod.event.KeyDown):
                        if event.sym == tcod.event.KeySym.Q:
                            self.is_running = False
                            break

                        w_pressed = event.sym == tcod.event.KeySym.W
                        s_pressed = event.sym == tcod.event.KeySym.S
                        a_pressed = event.sym == tcod.event.KeySym.A
                        d_pressed = event.sym == tcod.event.KeySym.D
                        horizontal_movement = 0
                        vertical_movement = 0

                        lock_movement = (
                            w_pressed and s_pressed and a_pressed and d_pressed
                        )
                        if lock_movement:
                            pass
                        elif w_pressed and not s_pressed:
                            vertical_movement = -1
                        elif s_pressed and not w_pressed:
                            vertical_movement = 1

                        if lock_movement:
                            pass
                        elif a_pressed and not d_pressed:
                            horizontal_movement = -1
                        elif d_pressed and not a_pressed:
                            horizontal_movement = 1

                        character.move(world, horizontal_movement, vertical_movement)

                        need_redraw = character.need_redraw

                    if need_redraw:
                        self.render(context, console, world, character)
