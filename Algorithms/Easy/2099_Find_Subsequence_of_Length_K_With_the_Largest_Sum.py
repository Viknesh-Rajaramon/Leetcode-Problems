from imports import *

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = sorted([(num, i) for i, num in enumerate(nums)], reverse = True)[ : k]
        arr.sort(key = lambda x: x[1])
        return [num for num, _ in arr]
