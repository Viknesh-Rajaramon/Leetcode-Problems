from typing import List
from math import inf

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        result, prev = 0, -inf

        for num in nums:
            if prev < num - k:
                prev = num - k
                result += 1
            elif prev < num + k:
                prev += 1
                result += 1
        
        return result
