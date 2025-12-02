from imports import *

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod, counts = 10**9 + 7, defaultdict(int)
        for _, y in points:
            counts[y] += 1

        total_sum, total_sq_sum = 0, 0
        for count in counts.values():
            if count < 2:
                continue
            
            f = count * (count - 1)
            total_sum += f
            total_sq_sum += f*f

        result = (total_sum * total_sum - total_sq_sum) // 8
        return result % mod
