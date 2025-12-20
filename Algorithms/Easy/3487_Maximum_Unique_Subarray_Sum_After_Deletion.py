from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s, curr_sum = set(), 0
        for n in nums:
            if n > 0 and n not in s:
                s.add(n)
                curr_sum += n

        if curr_sum == 0:
            return max(nums)
        
        return curr_sum
