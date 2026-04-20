from math import inf

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_, min_element = [0] * n, inf
        for i in range(n-1, -1, -1):
            min_element = min(min_element, nums[i])
            min_[i] = min_element
        
        max_ = 0
        for i in range(n):
            max_ = max(max_, nums[i])
            if max_ - min_[i] <= k:
                return i
        
        return -1
