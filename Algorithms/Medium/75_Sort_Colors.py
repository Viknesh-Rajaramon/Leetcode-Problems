from imports import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        idx = 0
        for color in range(3):
            for count in range(counts[color]):
                nums[idx] = color
                idx += 1
