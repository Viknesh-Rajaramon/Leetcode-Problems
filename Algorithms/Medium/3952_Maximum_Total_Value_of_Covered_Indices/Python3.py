from typing import List

class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        prev, curr = 0, nums[0] if s[0] == "1" else 0
        for i in range(1, len(nums)):
            if s[i] == "1":
                prev += nums[i-1]
                curr = max(curr+nums[i], prev)
            else:
                prev = curr
        
        return curr
