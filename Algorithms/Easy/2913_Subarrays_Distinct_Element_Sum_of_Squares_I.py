from imports import *

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                result += len(s)**2
        
        return result
