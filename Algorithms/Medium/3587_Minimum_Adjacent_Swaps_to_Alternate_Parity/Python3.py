from typing import List
from math import inf

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        even, odd = [], []
        for i in range(n):
            if nums[i] % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        if abs(len(even) - len(odd)) > 1:
            return -1
        
        def calculate_swaps(indices: List[int]):
            swaps = 0
            for i in range(len(indices)):
                swaps += abs(indices[i] - 2*i)

            return swaps

        swaps = inf
        if len(even) >= len(odd):
            swaps = min(swaps, calculate_swaps(even))
        if len(odd) >= len(even):
            swaps = min(swaps, calculate_swaps(odd))

        return swaps
