from imports import *

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        all_zero, result = True, 0
        for num in nums:
            result ^= num
            if num != 0:
                all_zero = False
        
        if all_zero:
            return 0

        return len(nums) - 1 if result == 0 else len(nums)
