from math import inf

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_max = [-inf] * n
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i+1])
        
        result, left_max = [], -inf
        for i in range(n):
            if nums[i] > left_max or nums[i] > right_max[i]:
                result.append(nums[i])
            
            left_max = max(left_max, nums[i])

        return result
