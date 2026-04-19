from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        ans, count = 1, 1
        n = len(nums)
        bits_set = nums[0]
        i = 0
        for j in range(1, n):
            if bits_set & nums[j] != 0:
                ans = max(ans, j-i)
                while bits_set & nums[j] != 0 and i < j:
                    bits_set = bits_set ^ nums[i]
                    i += 1
            
            bits_set = bits_set | nums[j]
        
        return max(ans, j-i+1)
