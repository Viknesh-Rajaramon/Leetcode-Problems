from math import gcd

class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        result, n, i = 1, len(nums), 0
        while i < n:
            r, j = nums[i]%k, i
            while j < n and nums[j]%k == r:
                j += 1
            
            g = k // gcd(r, k)
            result = max(result, 1 + ((j-i-1) // g) * g)
            i = j
        
        return result
