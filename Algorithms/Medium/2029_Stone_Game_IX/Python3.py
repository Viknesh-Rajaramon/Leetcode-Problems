from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]
        for val in stones:
            count[val%3] += 1
            
        if count[0] % 2 == 0:
            return count[1] >= 1 and count[2] >= 1

        return abs(count[1] - count[2]) > 2
