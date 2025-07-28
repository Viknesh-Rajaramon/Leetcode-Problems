from imports import *

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit_or = 0
        for num in nums:
            max_bit_or |= num
        
        n = len(nums)
        def count_subsets(index: int, curr: int) -> int:    
            if index == n:
                return 1 if curr == max_bit_or else 0
            
            return count_subsets(index+1, curr | nums[index]) + count_subsets(index+1, curr)
        
        return count_subsets(0, 0)
