from imports import *

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def dfs(i: int, product: int) -> bool:
            if product > target or i == len(nums):
                return False
                
            if product == target:
                return True
            
            return dfs(i+1, product * nums[i]) or dfs(i+1, product)

        product = 1
        for num in nums:
            product *= num
        
        if product != target**2:
            return False

        return dfs(0, 1)
