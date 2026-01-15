from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def get_max_consecutive_length(arr: List[int]) -> int:
            max_, curr = 1, 1
            for i in range(len(arr)-1):
                if arr[i+1] == arr[i]+1:
                    curr += 1
                    max_ = max(max_, curr)
                else:
                    curr = 1

            return max_
        
        side = min(get_max_consecutive_length(hBars), get_max_consecutive_length(vBars)) + 1
        return side * side
