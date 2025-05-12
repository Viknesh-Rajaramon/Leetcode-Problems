from imports import *

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        curr_sum = 0
        for n in nums:
            if curr_sum < curr_sum + n and n not in s:
                s.add(n)
                curr_sum += n

        if curr_sum == 0:
            return max(nums)
        
        return curr_sum
