from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum, left_sum = sum(nums), 0
        
        result = []
        for i in range(len(nums)):
            left_sum += nums[i]
            result.append(abs(total_sum - left_sum))
            total_sum -= nums[i]
        
        return result
