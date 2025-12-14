from imports import *

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        return sum(sorted(nums)[-k : ]) - sum(sorted(nums)[ : k])
