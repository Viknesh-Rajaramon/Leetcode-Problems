from imports import *

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n, left, right, count, result = len(nums), 0, 0, 0, 0
        for i, num in enumerate(nums):
            count += 1
            if i < n-1 and num == nums[i+1]:
                continue
            
            while left < n and nums[left] < num - k:
                left += 1
            
            while right < n and nums[right] <= num + k:
                right += 1
            
            result, count = max(result, min(right - left, count + numOperations)), 0
        
        if result >= numOperations:
            return result

        left = 0
        for right, num in enumerate(nums):
            while nums[left] < num - 2*k:
                left += 1
            
            result = max(result, right - left + 1)
        
        return min(result, numOperations)
