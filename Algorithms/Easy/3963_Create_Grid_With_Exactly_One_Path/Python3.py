class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        side_row, last_row = "." + "#" * (n-1), "." * n
        grid = [side_row] * (m-1)
        grid.append(last_row)
        return grid
