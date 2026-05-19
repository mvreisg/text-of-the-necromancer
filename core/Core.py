from blessed import Terminal

class Core:
    def __init__(self):
        pass
        
    def run(self):
        term = Terminal()

        with term.cbreak():
            key = term.inkey()
            print(f"You pressed: {key}")
    