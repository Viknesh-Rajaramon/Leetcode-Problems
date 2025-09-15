from imports import *

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        result, kept = 0, defaultdict(deque)
        for day, item in enumerate(arrivals):
            left = day - w
            while kept[item] and kept[item][0] <= left:
                kept[item].popleft()
            
            if len(kept[item]) == m:
                result += 1
            else:
                kept[item].append(day)

        return result
