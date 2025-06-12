from imports import *

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        sorted_nums = sorted([(nums[i], i) for i in range(n)])

        for i in range(1, n):
            if sorted_nums[i][0] != sorted_nums[i-1][0]:
                result[sorted_nums[i][1]] = i
            else:
                result[sorted_nums[i][1]] = result[sorted_nums[i-1][1]]
        
        return result
