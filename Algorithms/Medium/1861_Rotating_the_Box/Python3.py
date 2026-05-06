from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        result = [["."] * m for _ in range(n)]
        for i in range(m):
            bottom = n-1
            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == "#":
                    result[bottom][m-1-i] = "#"
                    bottom -= 1
                elif boxGrid[i][j] == "*":
                    result[j][m-1-i] = "*"
                    bottom = j-1

        return result
