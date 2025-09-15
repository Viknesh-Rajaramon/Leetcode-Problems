from imports import *

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        sum_, n = sum(nums), len(nums)
        i = sum_ // n + 1 if sum_ > 0 else 1
        while i in nums:
            i += 1
        
        return i
