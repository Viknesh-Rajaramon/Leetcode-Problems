from imports import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid-1] < target and target < nums[mid]:
                return mid
            elif nums[mid] < target and mid+1 < len(nums) and target < nums[mid+1]:
                return mid+1
            elif target < nums[mid]:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        
        return low
