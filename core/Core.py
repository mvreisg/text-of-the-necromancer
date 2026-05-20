from blessed import Terminal

from core.model.World import World

class Core:
    def __init__(self) -> None:
        self.is_running = True
        self.x = 0
        self.y = 0
        
    def run(self) -> None:
        term = Terminal()

        world = World(50, 50)
        world.generate()

        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            while self.is_running:
                key = term.inkey(timeout=0.016)

                if key.code == term.KEY_LEFT:
                    self.x -= 1

                if key.code == term.KEY_RIGHT:
                    self.x += 1                    

                if key.code == term.KEY_UP:
                    self.y -= 1

                if key.code == term.KEY_DOWN:
                    self.y += 1                                        

                if self.x < 0:
                    self.x = 0

                if self.x > 49:
                    self.x = 49

                if self.y < 0:
                    self.y = 0 

                if self.y > 49:
                    self.y = 49                                       

                print(
                    term.home + term.clear, 
                    end=""
                )

                for x in range(49):
                    for y in range(49):
                        print(
                            term.move_xy(x, y) + term.white("#"),
                            end="",
                            flush=True
                        )   

                print(
                    term.move_xy(self.x, self.y) + term.green("@"),
                    end="",
                    flush=True
                )

    