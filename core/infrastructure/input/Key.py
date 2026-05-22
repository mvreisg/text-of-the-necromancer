class Key:
    def __init__(self) -> None:
        self.is_pressed = False

    def set_is_pressed(self, is_pressed: bool) -> None:
        self.is_pressed = is_pressed

    def get_is_pressed(self) -> bool:
        return self.is_pressed
