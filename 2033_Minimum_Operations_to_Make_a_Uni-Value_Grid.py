from imports import *

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])        
        nums = [grid[i][j] for i in range(m) for j in range(n)]
        nums.sort()

        common = nums[0] % x
        mid = len(nums)//2
        if not all(ele%x == common for ele in nums):
            return -1
        
        diff = 0
        for i in range(0, mid):
            diff += nums[mid] - nums[i]
        
        for i in range(mid+1, len(nums)):
            diff += nums[i] - nums[mid]
        
        return diff // x
