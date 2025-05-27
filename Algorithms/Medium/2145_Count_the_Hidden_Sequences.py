from imports import *

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        nums = list(accumulate(differences, initial = 0))
        return max(0, upper - lower - max(nums) + min(nums) + 1)
