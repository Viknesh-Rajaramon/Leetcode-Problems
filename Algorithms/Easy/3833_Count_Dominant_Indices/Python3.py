from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        result, sum_, count = 0, nums[-1], 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > sum_/count:
                result += 1
            
            sum_ += nums[i]
            count += 1

        return result
