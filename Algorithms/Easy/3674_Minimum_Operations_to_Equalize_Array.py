from imports import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 0 if all(x == nums[0] for x in nums) else 1
