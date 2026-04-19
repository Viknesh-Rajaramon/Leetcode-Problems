from typing import List
from math import inf, sqrt

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        divisors = set()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        
        divisors = sorted(divisors)

        min_diff, result = inf, None
        def dfs(pos: int, last: int, rem: int, min_: int, max_: int, path: List[int]):
            nonlocal min_diff, result
            
            if pos == k-1:
                if rem < last:
                    return
                
                min_ = min(min_, rem)
                max_ = max(max_, rem)
                diff = max_ - min_
                if diff < min_diff:
                    min_diff = diff
                    result = path + [rem]
                
                return
            
            for d in divisors:
                if d < last or rem % d != 0:
                    continue
                
                nxt_min, nxt_max = min(min_, d), max(max_, d)
                if nxt_max - nxt_min >= min_diff:
                    continue
                
                dfs(pos+1, d, rem // d, nxt_min, nxt_max, path + [d])

        dfs(0, 1, n, inf, 0, [])
        return result
