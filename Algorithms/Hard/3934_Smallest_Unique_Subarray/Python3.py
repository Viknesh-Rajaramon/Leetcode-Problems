from typing import List
from collections import defaultdict

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n, mod, base = len(nums), (1<<61)-1, 10**5+5
        def check(length: int) -> bool:
            power, h = pow(base, length, mod), 0
            for i in range(length):
                h = (h*base + nums[i]) % mod
            
            f = defaultdict(int)
            f[h] += 1

            for i in range(1, n-length+1):
                h = (h*base - nums[i-1]*power + nums[i+length-1]) % mod
                f[h] += 1
            
            return any(x == 1 for x in f.values())

        low, high = 1, n
        while low < high:
            mid = (low+high)//2
            if check(mid):
                high = mid
            else:
                low = mid+1
        
        return low
