from imports import *

class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def _getIntValue(self, X: str) -> int:
        if ord("A") <= ord(X[0]) <= ord("Z"):
            return self.spreadsheet[X]
        
        return int(X)

    def getValue(self, formula: str) -> int:
        X, Y = formula[1:].split("+")
        return self._getIntValue(X) + self._getIntValue(Y)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
