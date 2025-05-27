from imports import *

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        def getPos():
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] > 0:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return n-low

        def getNeg():
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] < 0:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return high+1

        return max(getPos(), getNeg())
