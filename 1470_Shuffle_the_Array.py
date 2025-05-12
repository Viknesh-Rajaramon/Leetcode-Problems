from imports import *

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        for i in range(0, n):
            new_nums.append(nums[i])
            new_nums.append(nums[n+i])
        
        return new_nums
