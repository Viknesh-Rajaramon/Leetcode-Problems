from imports import *

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        max_count = 0

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                max_count += 1
                i += 1
                j += 1
            else:
                j += 1

        return max_count
