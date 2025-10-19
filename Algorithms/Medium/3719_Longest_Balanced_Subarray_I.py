from imports import *

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        for i in range(n):
            even, odd = set(), set()
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                
                if len(even) == len(odd):
                    result = max(result, j-i+1)
        
        return result
