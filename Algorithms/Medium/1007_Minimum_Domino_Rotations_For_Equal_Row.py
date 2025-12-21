from typing import List
from math import inf

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = inf

        for num in range(1, 7):
            top_swaps, bottom_swaps = 0, 0
            valid = True

            for top, bottom in zip(tops, bottoms):
                if top != num and bottom != num:
                    valid = False
                    break
                
                if top != num:
                    top_swaps += 1
                
                if bottom != num:
                    bottom_swaps += 1
            
            if valid:
                result = min(result, top_swaps, bottom_swaps)
        
        return -1 if result == inf else result
