from imports import *

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num)*abs(num) for num in nums]
        nums.sort(reverse = True)
        k = ceil(len(nums) / 2)
        return sum(nums[:k]) - sum(nums[k:])
