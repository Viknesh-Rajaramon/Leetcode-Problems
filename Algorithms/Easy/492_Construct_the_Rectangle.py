from imports import *

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for W in range(int(sqrt(area)), 0, -1):
            L = area // W
            if L*W == area:
                return [L, W]
        
        return [area, 1]
