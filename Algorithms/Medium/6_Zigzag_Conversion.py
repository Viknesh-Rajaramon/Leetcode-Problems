from imports import *

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]

        direction = 1
        row = 0
        for c in s:
            rows[row].append(c)
            row += direction

            if row == 0 or row == numRows - 1:
                direction *= -1
        
        return "".join(["".join(row) for row in rows])
