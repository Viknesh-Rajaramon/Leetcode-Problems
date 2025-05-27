from imports import *

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [0] * n
        left[0] = nums[0]
        for i in range(n-2):
            left[i+1] = max(left[i], nums[i])
        
        right = [0] * n
        right[-1] = nums[-1]
        for i in reversed(range(n-1)):
            right[i] = min(right[i+1], nums[i+1])

        beauty = 0
        for i in range(1, n-1):
            if left[i] < nums[i] < right[i]:
                beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1

        return beauty
