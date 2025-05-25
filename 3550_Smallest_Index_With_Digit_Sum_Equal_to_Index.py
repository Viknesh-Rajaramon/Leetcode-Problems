from imports import *

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_of_digits(num: int) -> int:
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
                
            return result

        for i in range(len(nums)):
            if i == sum_of_digits(nums[i]):
                return i

        return -1
