from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_sum(index: int, current_xor_sum: int) -> int:
            if index == len(nums):
                return current_xor_sum

            return xor_sum(index+1, current_xor_sum) + xor_sum(index+1, current_xor_sum ^ nums[index])
        
        return xor_sum(0, 0)
