from typing import List

class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        result = set()
        for num, t in zip(nums, target):
            if num != t:
                result.add(num)
        
        return len(result)
