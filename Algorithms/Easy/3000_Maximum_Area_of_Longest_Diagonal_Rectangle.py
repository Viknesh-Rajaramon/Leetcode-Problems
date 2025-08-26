from imports import *

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area, max_diagnol = 0, 0
        for l, w in dimensions:
            diagnol = l*l + w*w
            if diagnol > max_diagnol:
                max_diagnol = diagnol
                max_area = l*w
            elif diagnol == max_diagnol:
                area = l*w
                if area > max_area:
                    max_area = area
        
        return max_area
