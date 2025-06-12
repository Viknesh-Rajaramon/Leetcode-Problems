from imports import *

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        result = sum(nums)

        for num in nums:
            while num > 0:
                result -= num % 10
                num //= 10
        
        return result
