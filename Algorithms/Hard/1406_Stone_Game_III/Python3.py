from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        s1, s2, s3, tot = 0, 0, 0, 0
        for val in reversed(stoneValue):
            tot += val
            s1, s2, s3 = tot - min(s1,s2,s3), s1, s2
        
        if 2*s1 > tot:
            return "Alice"
        elif 2*s1 < tot:
            return "Bob"
        
        return "Tie"
