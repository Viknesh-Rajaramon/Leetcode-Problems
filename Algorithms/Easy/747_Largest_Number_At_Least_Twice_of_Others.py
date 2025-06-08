from imports import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max, second_max = 0, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[first_max]:
                second_max = first_max
                first_max = i
            elif second_max == -1 or nums[second_max] < nums[i] < nums[first_max]:
                second_max = i
        
        return -1 if second_max == -1 or nums[first_max] < 2*nums[second_max] else first_max
