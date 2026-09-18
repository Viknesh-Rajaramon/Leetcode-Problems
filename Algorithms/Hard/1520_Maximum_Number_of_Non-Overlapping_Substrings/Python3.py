from math import inf
from collections import deque

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        counts, first, last = {}, {}, {}
        for i, c in enumerate(s):
            if c not in counts:
                counts[c] = 0
                first[c] = i
            
            counts[c] += 1
            last[c] = i
        
        result, queue = [], deque()
        for k in counts:
            queue.appendleft([first[k], last[k], counts[k]])
            l, r, total = inf, -inf, 0
            for x, y, z in queue:
                total += z
                l = min(l, x)
                r = max(r, y)
                if total == r-l+1:
                    break

            if total == r-l+1:
                result.append(s[l : r+1])
                queue = deque()

        return result
