from imports import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_indices = []
        
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                if len(zero_indices) > 0:
                    index = zero_indices.pop(0)
                    nums[index] = nums[i]
                    nums[i] = 0
                    zero_indices.append(i)
                else:
                    pass
            else:
                zero_indices.append(i)
