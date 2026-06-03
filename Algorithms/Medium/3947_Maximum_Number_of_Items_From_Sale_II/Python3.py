from typing import List
from collections import Counter
from math import inf

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n, vals = len(items), [item[0] for item in items]
        freq, mx, factor = Counter(vals), max(vals), {}
        for v in freq:
            factor[v] = sum(freq[m] for m in range(v, mx+1, v) if m in freq) - 1
        
        pre, mn = [], inf
        for i in range(n):
            v, cost = items[i]
            c, mn = factor[v], min(mn, cost)
            pre.append([v, cost, c, cost/(2 if c > 0 else 1)])
        
        pre.sort(key = lambda x: (x[3], -x[2]))
        result, cnt = budget//mn, 0
        for _, y, z, _ in pre:
            c = min(z, budget//y)
            cnt += c << 1
            budget -= c*y
            result = max(result, cnt + (budget//mn))

        return result
