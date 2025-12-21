class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+")

        if x in self.spreadsheet:
            x_val = self.spreadsheet[x]
        else:
            if x.isdigit():
                x_val = int(x)
            else:
                x_val = 0

        if y in self.spreadsheet:
            y_val = self.spreadsheet[y]
        else:
            if y.isdigit():
                y_val = int(y)
            else:
                y_val = 0

        return x_val + y_val


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
