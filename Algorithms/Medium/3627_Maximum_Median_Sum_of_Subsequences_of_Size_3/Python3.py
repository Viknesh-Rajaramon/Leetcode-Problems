from typing import List

class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums) // 3
        return sum(nums[1 : 2*n + 1 : 2])
