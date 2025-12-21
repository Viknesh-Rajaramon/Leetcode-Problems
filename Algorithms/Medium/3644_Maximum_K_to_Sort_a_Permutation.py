from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        result, flag = 0, False
        for i in range(len(nums)):
            if nums[i] != i:
                if not flag:
                    result = nums[i]
                    flag = True
                else:
                    result &= nums[i]
        
        return result if flag else 0
