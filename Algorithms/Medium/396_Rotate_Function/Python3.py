from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        f, sum_ = sum(i*nums[i] for i in range(n)), sum(nums)
        
        result = f
        for i in range(n-1, 0, -1):
            f += sum_ - n*nums[i]
            result = max(result, f)

        return result
