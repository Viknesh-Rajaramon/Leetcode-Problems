from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        stack = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                max_len = max(max_len, len(stack))
                stack = [nums[i]]
        
        return max(max_len, len(stack))
