from pathlib import Path
import tcod
from core.model.Character import Character

from core.model.World import World

class Core:
    def __init__(self) -> None:
        self.is_running = True
        self.row = 0
        self.column = 0

    def run(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        FONT_PATH = BASE_DIR / "assets/fonts/terminal16x16_gs_ro.png"
        tileset = tcod.tileset.load_tilesheet(
            FONT_PATH,
            16,
            16,
            tcod.tileset.CHARMAP_CP437
        )
        world = World(
            rows=40, 
            columns=40
        )
        character = Character(
            x=0,
            y=0            
        )
        world.generate()

        with tcod.context.new_terminal(
            columns=world.columns,
            rows=world.rows,
            tileset=tileset,
            title="Text of The Necromancer"
        ) as context:
            console = tcod.console.Console(
                width=world.columns, 
                height=world.rows
            )
            while self.is_running:
                console.clear()

                for r in range(world.rows):
                    for c in range(world.columns):
                        cell = world.get_cell(r, c)
                        console.print(
                            cell.x,
                            cell.y,
                            cell.char,
                            fg=cell.color
                    )

                console.print(
                    character.x, 
                    character.y, 
                    character.char,
                    fg=character.color
                )

                context.present(console)

                for event in tcod.event.wait():
                    if event.type == "QUIT":
                        self.is_running = False
                        break     

                    if isinstance(event, tcod.event.KeyDown):
                        if (event.sym == tcod.event.KeySym.W):
                            character.move(world, 0, -1)
                        elif (event.sym == tcod.event.KeySym.S):
                            character.move(world, 0, 1)
                        elif (event.sym == tcod.event.KeySym.A):
                            character.move(world, -1, 0)
                        elif (event.sym == tcod.event.KeySym.D):
                            character.move(world, 1, 0)                                                                                    

        
    