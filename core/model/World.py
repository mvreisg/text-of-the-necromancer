from core.model.Cell import Cell


class World:
    def __init__(
        self, 
        width: int, 
        height: int
    ) -> None:
        self.width = width
        self.height = height
        self.cells: list[list[Cell]] = []
    
    def generate(self):
        for y in range(self.height):
            row: list[Cell] = []
            for x in range(self.width):
                row.append(Cell(x, y, '#', 'white'))
            self.cells.append(row)