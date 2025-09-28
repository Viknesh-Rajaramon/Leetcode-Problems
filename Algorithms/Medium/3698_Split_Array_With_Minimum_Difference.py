from imports import *

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right, left_sum, right_sum = 1, n-2, 0, 0

        while left < n and nums[left] > nums[left-1]:
            left_sum += nums[left-1]
            left += 1
        
        left -= 1
        left_sum += nums[left]

        while right >= 0 and nums[right] > nums[right+1]:
            right_sum += nums[right+1]
            right -= 1
        
        right += 1

        if right != left:
            right_sum += nums[right]
        
        if right - left > 1:
            return -1
        
        result = abs(left_sum - right_sum)
        if left > 0:
            left_sum -= nums[left]
            right_sum += nums[left]
            result = min(result, abs(left_sum - right_sum))
        
        return result
