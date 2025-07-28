from imports import *

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bit_or = 0
        for num in nums:
            max_bit_or |= num
        
        n = len(nums)
        def count_subsets(i: int, curr: int) -> int:    
            if i == n:
                return 1 if curr == max_bit_or else 0
            
            return count_subsets(i + 1, curr | nums[i]) + count_subsets(i + 1, curr)

        return count_subsets(0, 0)
