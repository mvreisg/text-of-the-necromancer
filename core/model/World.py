from core.model.Cell import Cell


class World:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.cells: list[list[Cell]] = []

    def generate(self):
        for r in range(self.rows):
            columns: list[Cell] = []
            for c in range(self.columns):
                columns.append(Cell(c, r, "#", True))
            self.cells.append(columns)

    def get_cell(self, row: int, column: int) -> Cell:
        return self.cells[row][column]

    def get_redraw_state(self, row: int, column: int) -> bool:
        return self.get_cell(row, column).need_redraw

    def set_redraw_state(self, row: int, column: int, need_redraw: bool) -> None:
        self.cells[row][column].set_redraw_state(need_redraw)
