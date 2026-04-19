from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        result = 0
        i, j = 0, len(nums)-1
        while i < j:
            result = max(result, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return result
