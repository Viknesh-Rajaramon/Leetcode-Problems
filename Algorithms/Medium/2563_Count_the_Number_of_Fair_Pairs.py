from imports import *

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def lower_bound(low, high, num) -> int:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= num:
                    high = mid - 1
                else:
                    low = mid + 1

            return low
        
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n):
            count += lower_bound(i+1, n-1, upper - nums[i] + 1) - lower_bound(i+1, n-1, lower - nums[i])

        return count
