from imports import *

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        if m == n:
            return min(batteries)
        
        batteries.sort()
        s, l = sum(batteries[:-n]), batteries[-n:]
        for i in range(1, n):
            diff = (l[i] - l[i-1]) * i
            if s < diff:
                return l[i-1] + s // i
            
            s -= diff

        return l[-1] + s // n
