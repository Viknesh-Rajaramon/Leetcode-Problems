from imports import *

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for key, count in Counter(nums).items():
            if count > len(nums) // 3:
                result.append(key)
        
        return result
