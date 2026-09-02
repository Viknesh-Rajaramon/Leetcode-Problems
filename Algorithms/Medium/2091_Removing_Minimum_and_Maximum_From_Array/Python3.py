from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n, min_idx, max_idx = len(nums), 0, 0
        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            
            if nums[i] > nums[max_idx]:
                max_idx = i
            
        l, r = min(min_idx, max_idx), max(min_idx, max_idx)
        return min(r+1, n-l, l+1+n-r)
