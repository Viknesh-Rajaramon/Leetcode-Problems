from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                prefix[i] = prefix[i-1] + 1
            
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                suffix[i] = suffix[i+1] + 1
        
        result, replacements = max(max(prefix), max(suffix)), 1
        for i in range(1, n-1):
            if nums[i-1] <= nums[i+1]:
                new = 1+prefix[i-1]+suffix[i+1]
                if new > result:
                    result, replacements = new, 0

        return min(n, result+replacements)
