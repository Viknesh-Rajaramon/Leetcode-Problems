from imports import *

class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def fillQuadrant(n: int, offset: int):
            if n == 0:
                return [[offset]]

            size = 2**(2*(n-1))
            top_right = fillQuadrant(n-1, offset)
            bottom_right = fillQuadrant(n-1, offset+size)
            bottom_left = fillQuadrant(n-1, offset+2*size)
            top_left = fillQuadrant(n-1, offset+3*size)

            quadrant_range = len(top_right)
            grid = [[0] * (2*quadrant_range) for _ in range(2*quadrant_range)]

            for i in range(quadrant_range):
                for j in range(quadrant_range):
                    grid[i][j+quadrant_range] = top_right[i][j]
                    grid[i+quadrant_range][j+quadrant_range] = bottom_right[i][j]
                    grid[i+quadrant_range][j] = bottom_left[i][j]
                    grid[i][j] = top_left[i][j]

            return grid

        return fillQuadrant(N, 0)
