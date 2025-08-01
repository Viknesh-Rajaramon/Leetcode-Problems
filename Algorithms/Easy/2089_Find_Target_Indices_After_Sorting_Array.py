from imports import *

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
            elif nums[i] > target:
                break
        
        return result
