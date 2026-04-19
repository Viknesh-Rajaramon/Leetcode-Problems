from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            x = num % 3
            result += min(x, 3 - x)
        
        return result
