from imports import *

class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        d = defaultdict(list)
        for l, v in zip(limit, value):
            d[l].append(v)
        
        result = 0
        for j, m in d.items():
            if j >= len(m):
                result += sum(m)
            else:
                m.sort(reverse = True)
                result += sum(m[ : j])

        return result
