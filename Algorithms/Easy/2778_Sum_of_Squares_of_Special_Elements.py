from imports import *

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            if n % (i+1) == 0:
                result += nums[i]*nums[i]

        return result
