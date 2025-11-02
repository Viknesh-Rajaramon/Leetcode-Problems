from imports import *

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def can_deliver(T: int) -> bool:
            c1, c2, lcm = T - T // r[0], T - T // r[1], r[0] * r[1] // gcd(r[0], r[1])
            total = T - T // lcm
            return c1 >= d[0] and c2 >= d[1] and sum(d) <= total
        
        low, high = 0, 10**10
        while low < high:
            mid = (low + high) // 2
            if can_deliver(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
