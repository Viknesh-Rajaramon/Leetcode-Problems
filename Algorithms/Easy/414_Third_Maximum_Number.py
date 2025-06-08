from imports import *

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max, second_max, third_max = nums[0], -inf, -inf
        for i in range(1, len(nums)):
            if nums[i] in [first_max, second_max, third_max] or nums[i] <= third_max:
                continue
             
            if nums[i] > first_max:
                third_max = second_max
                second_max = first_max
                first_max = nums[i]
            elif nums[i] > second_max:
                third_max = second_max
                second_max = nums[i]
            else:
                third_max = nums[i]
        
        return third_max if third_max != -inf else first_max
