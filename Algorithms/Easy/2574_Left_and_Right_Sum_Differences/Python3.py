from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result, total_sum, left_sum = [], sum(nums), 0
        for num in nums:
            left_sum += num
            result.append(abs(total_sum - left_sum))
            total_sum -= num
        
        return result
