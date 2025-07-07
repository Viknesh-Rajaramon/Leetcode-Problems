from imports import *

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])

        fa = list(range(events[-1][1] + 2))
        def find(x: int) -> int:
            if x != fa[x]:
                fa[x] = find(fa[x])
            
            return fa[x]

        result = 0
        for start, end in events:
            t = find(start)
            if t <= end:
                result += 1
                fa[t] = t + 1

        return result
