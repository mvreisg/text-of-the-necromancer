from blessed.terminal import Terminal

from core.model.World import World

class Core:
    def __init__(self) -> None:
        self.is_running = True
        self.row = 0
        self.column = 0

    def run(self) -> None:
        term = Terminal()

        world = World(
            rows=50, 
            columns=100
        )
        world.generate()

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            while self.is_running:
                key = term.inkey(timeout=0.016)

                if key == "q":
                    self.is_running = False
                    break     

                if key.code == term.KEY_LEFT:
                    world.invalidate()
                    self.column -= 1

                if key.code == term.KEY_RIGHT:
                    world.invalidate()
                    self.column += 1                    

                if key.code == term.KEY_UP:
                    world.invalidate()
                    self.row -= 1

                if key.code == term.KEY_DOWN:
                    world.invalidate()
                    self.row += 1                                        

                if self.row < 0:
                    self.row = 0

                if self.column < 0:
                    self.column = 0

                if self.column > world.columns - 1:
                    self.column = world.columns - 1

                if self.row > world.rows - 1:
                    self.row = world.rows - 1            

                if world.is_valid == False:                    
                    print(
                        term.home + term.clear, 
                        end=""
                    )

                    world_as_string = ""

                    for row in range(world.rows):
                        for column in range(world.columns):
                            world_as_string += term.white(world.get_cell(row, column).char)
                        world_as_string += "\n"

                    print(
                        world_as_string,
                        end="",
                        flush=True
                    ) 

                    print(
                        term.move_xy(self.column, self.row) + term.green("@"),
                        end="",
                        flush=True
                    )

                    world.validate()

    