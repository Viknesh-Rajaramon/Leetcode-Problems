from typing import List

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        vis, stack = 0, []
        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
                vis += 1
            
            if stack:
                vis += 1
            
            stack.append(num)

        return vis - len(nums) + 1
