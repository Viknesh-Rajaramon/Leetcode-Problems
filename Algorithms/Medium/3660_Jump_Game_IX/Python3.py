from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        result, n = [nums[0]], len(nums)
        for i in range(1, n):
            result.append(max(result[-1], nums[i]))
        
        curr = n-1
        for i in range(n-2, -1, -1):
            if result[i] > nums[curr]:
                result[i] = result[curr]
            
            if nums[i] < nums[curr]:
                curr = i
        
        return result
