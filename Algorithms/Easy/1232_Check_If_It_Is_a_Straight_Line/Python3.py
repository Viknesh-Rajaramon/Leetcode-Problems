from typing import List
from math import inf

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        m = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else inf

        for x, y in coordinates[2 : ]:
            new_slope = (y - y1) / (x - x1) if x - x1 != 0 else inf
            if new_slope != m:
                return False
        
        return True
