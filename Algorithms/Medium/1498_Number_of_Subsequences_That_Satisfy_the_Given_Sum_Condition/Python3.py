from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        j = n-1

        result = 0
        for i in range(n):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1

            if j < i:
                break
            
            result = (result + pow(2, j-i, mod)) % mod
        
        return result
