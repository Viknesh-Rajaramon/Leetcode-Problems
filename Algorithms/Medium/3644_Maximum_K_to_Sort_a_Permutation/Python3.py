from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        result, flag = 0, False
        for i, num in enumerate(nums):
            if num == i:
                continue
            
            if not flag:
                result = num
                flag = True
            else:
                result &= num
        
        return result if flag else 0
