from imports import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        n = len(nums)
        
        low, high = 0, n-1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] == target:
                high = mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if nums[low] != target:
            return [-1, -1]
        
        min_index = low

        low, high = 0, n-1
        max_index = 0
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                max_index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return [min_index, max_index]