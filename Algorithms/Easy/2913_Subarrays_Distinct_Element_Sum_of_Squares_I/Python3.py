from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result, n = 0, len(nums)
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                result += len(s)**2
        
        return result
