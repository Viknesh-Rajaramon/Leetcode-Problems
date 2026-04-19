from typing import List

class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        left = [2] * n
        for i in range(n-2):
            if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
                left[i+2] = left[i+1] + 1
        
        right = [2] * n
        for i in range(n-3, -1, -1):
            if nums[i+2]-nums[i+1] == nums[i+1]-nums[i]:
                right[i] = right[i+1] + 1
        
        result = max(max(left), max(right)) + 1
        for i in range(1, n-1):
            if (nums[i+1] - nums[i-1])%2:
                continue
            
            diff = (nums[i+1] - nums[i-1]) // 2
            l, r = 1, 1
            if i >= 2 and nums[i-1] - nums[i-2] == diff:
                l = left[i-1]
            
            if i+2 < n and nums[i+2] - nums[i+1] == diff:
                r = right[i+1]
            
            result = max(result, l+r+1)

        return min(result, n)
