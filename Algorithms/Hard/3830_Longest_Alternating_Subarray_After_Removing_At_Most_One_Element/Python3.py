from typing import List

class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [[1] * n for _ in range(2)], [[1] * n for _ in range(2)]
        for i in range(n-1):
            left[0][i+1] = (left[1][i] + 1) if nums[i+1] > nums[i] else 1
            left[1][i+1] = (left[0][i] + 1) if nums[i+1] < nums[i] else 1
        
        for i in range(n-2, -1, -1):
            right[0][i] = (right[1][i+1] + 1) if nums[i] > nums[i+1] else 1
            right[1][i] = (right[0][i+1] + 1) if nums[i] < nums[i+1] else 1

        result = 0
        for i in range(n):
            result = max(result, left[0][i] + right[0][i] - 1, left[1][i] + right[1][i] - 1)
        
        for i in range(1, n-1):
            if nums[i-1] > nums[i+1]:
                result = max(result, left[0][i-1] + right[1][i+1])
            elif nums[i] < nums[i+1]:
                result = max(result, left[1][i-1] + right[0][i+1])
        
        return result
