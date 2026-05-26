import time
import tcod
from pathlib import Path
from core.graphics.Viewport import Viewport
from core.infrastructure.input.KeyCode import KeyCode
from core.infrastructure.input.Keyboard import Keyboard
from core.model.World import World


class Core:
    def __init__(self) -> None:
        self.is_running = True

    def run(self) -> None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        FONT_PATH = BASE_DIR / "assets/fonts/terminal16x16_gs_ro.png"
        tileset = tcod.tileset.load_tilesheet(
            FONT_PATH, 16, 16, tcod.tileset.CHARMAP_CP437
        )
        TARGET_FPS = 60.0
        TIME_PER_FRAME = 1.0 / TARGET_FPS

        viewport = Viewport(0, 0, 32, 32)
        viewport.generate()
        keyboard = Keyboard()
        world = World()

        with tcod.context.new(
            columns=viewport.width,
            rows=viewport.height,
            tileset=tileset,
            title="Text of The Necromancer",
        ) as context:
            console = tcod.console.Console(width=viewport.width, height=viewport.height)

            console.clear()

            world.create_area("test", 0, 0)
            area = world.get_area("test")
            for x in range(100):
                for y in range(100):
                    area.create_cell(x, y, "#", (255, 255, 255))

            area.create_character(0, 0, "@", (255, 0, 0))

            last_time = time.perf_counter()

            while self.is_running:
                for event in tcod.event.get():
                    if isinstance(event, tcod.event.MouseMotion):
                        continue
                    elif isinstance(event, tcod.event.KeyDown):
                        match event.sym:
                            case tcod.event.KeySym.Q:
                                keyboard.set_pressed(KeyCode.Q, True)
                            case tcod.event.KeySym.W:
                                keyboard.set_pressed(KeyCode.W, True)
                            case tcod.event.KeySym.S:
                                keyboard.set_pressed(KeyCode.S, True)
                            case tcod.event.KeySym.A:
                                keyboard.set_pressed(KeyCode.A, True)
                            case tcod.event.KeySym.D:
                                keyboard.set_pressed(KeyCode.D, True)
                            case _:
                                pass
                    elif isinstance(event, tcod.event.KeyUp):
                        match event.sym:
                            case tcod.event.KeySym.Q:
                                keyboard.set_pressed(KeyCode.Q, False)
                            case tcod.event.KeySym.W:
                                keyboard.set_pressed(KeyCode.W, False)
                            case tcod.event.KeySym.S:
                                keyboard.set_pressed(KeyCode.S, False)
                            case tcod.event.KeySym.A:
                                keyboard.set_pressed(KeyCode.A, False)
                            case tcod.event.KeySym.D:
                                keyboard.set_pressed(KeyCode.D, False)
                            case _:
                                pass

                if keyboard.get_pressed(KeyCode.Q):
                    self.is_running = False
                    break

                console.clear()

                delta = time.perf_counter() - last_time
                world.tick(keyboard, viewport, delta)
                world.render(viewport)
                if delta < TIME_PER_FRAME:
                    time.sleep(TIME_PER_FRAME - delta)

                for y in range(viewport.height):
                    for x in range(viewport.width):
                        unit = viewport.get(x, y)
                        if unit.is_valid == False:
                            console.print(
                                x=unit.x, y=unit.y, text=unit.character, fg=unit.color
                            )
                            viewport.validate(x, y)

                context.present(console=console, integer_scaling=True, keep_aspect=True)

                last_time = time.perf_counter()
