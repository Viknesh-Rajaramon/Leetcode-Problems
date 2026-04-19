from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        left = 0
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i+1]:
                if (nums[i] > nums[i+1] and nums[i] > nums[left]) or (nums[i] < nums[i+1] and nums[i] < nums[left]):
                    result += 1
                left = i
        
        return result
