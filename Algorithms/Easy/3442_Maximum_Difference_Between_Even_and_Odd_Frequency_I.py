from imports import *

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_val, min_val = -inf, inf
        for f in freq.values():
            if f % 2 == 1:
                max_val = max(max_val, f)
            else:
                min_val = min(min_val, f)

        return max_val - min_val
