from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot() -> int:
            low, high = 0, n-1
            while low < high:
                mid = (low+high) // 2
                
                if nums[0] <= nums[mid]:
                    low = mid + 1
                else:
                    high = mid
            
            return low
        
        def binary_search(low: int, high: int) -> int:
            while low <= high:
                mid = (low+high) // 2
                if nums[mid] == target:
                        return mid
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return -1

        n = len(nums)
        pivot_index = find_pivot()

        if nums[pivot_index] <= target <= nums[-1]:
            return binary_search(pivot_index, n-1)
        
        return binary_search(0, pivot_index-1)
