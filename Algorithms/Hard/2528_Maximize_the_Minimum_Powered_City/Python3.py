from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        count = [0] * (n+1)
        for i in range(n):
            count[max(0, i-r)] += stations[i]
            count[min(n, i+r+1)] -= stations[i]

        def check(val: int) -> bool:
            diff, total, remaining = count[:], 0, k
            for i in range(n):
                total += diff[i]
                if total < val:
                    add = val - total
                    if remaining < add:
                        return False
                    
                    remaining -= add
                    diff[min(n, i+2*r+1)] -= add
                    total += add
                
            return True
        
        low, high = min(stations), sum(stations)+k
        while low <= high:
            mid = (low+high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
