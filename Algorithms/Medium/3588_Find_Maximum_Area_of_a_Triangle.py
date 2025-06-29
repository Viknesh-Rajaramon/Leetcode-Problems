from imports import *

class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        min_x, max_x = inf, -inf
        min_y, max_y = inf, -inf
        x_to_y = defaultdict(lambda : [inf, -inf])
        y_to_x = defaultdict(lambda : [inf, -inf])

        for x, y in coords:
            x_to_y[x] = [min(x_to_y[x][0], y), max(x_to_y[x][1], y)]
            y_to_x[y] = [min(y_to_x[y][0], x), max(y_to_x[y][1], x)]

            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
        
        max_area = 0
        for x, y_ in x_to_y.items():
            base = y_[1] - y_[0]
            max_area = max(max_area, base * (max_x - x), base * (x - min_x))
        
        for y, x_ in y_to_x.items():
            base = x_[1] - x_[0]
            max_area = max(max_area, base * (max_y - y), base * (y - min_y))
        
        return max_area if max_area > 0 else -1
