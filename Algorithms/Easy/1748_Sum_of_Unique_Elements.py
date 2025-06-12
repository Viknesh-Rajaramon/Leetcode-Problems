from imports import *

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(val for val, count in Counter(nums).items() if count == 1)
