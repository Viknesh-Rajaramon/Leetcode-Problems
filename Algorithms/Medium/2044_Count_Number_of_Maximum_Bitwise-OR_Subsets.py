from imports import *

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit_or = 0
        for num in nums:
            max_bit_or |= num
        
        n = len(nums)
        result = 0

        def count_subsets(index: int, curr_bit_or: int) -> None:    
            nonlocal result
            if index == n:
                if curr_bit_or == max_bit_or:
                    result += 1
                
                return
            
            count_subsets(index+1, curr_bit_or | nums[index])
            count_subsets(index+1, curr_bit_or)
        
        count_subsets(0, 0)
        return result
