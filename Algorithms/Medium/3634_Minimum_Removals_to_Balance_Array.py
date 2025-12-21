from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i, count = 0, 0
        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1
            
            count = max(count, j - i + 1)
        
        return n - count
