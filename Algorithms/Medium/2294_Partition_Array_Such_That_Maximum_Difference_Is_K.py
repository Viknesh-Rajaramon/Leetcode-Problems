from imports import *

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        partitions = 1
        max_value = nums[0] + k
        
        for i in range(1, len(nums)):
            if nums[i] > max_value:
                partitions += 1
                max_value = nums[i] + k
        
        return partitions
