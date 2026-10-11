from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                result += nums[i]*nums[i]

        return result
