from typing import List
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        count = Counter([0])
        result = 0
        prefix_sum = 0
        for i in range(n):
            prefix_sum += 1 if nums[i] % modulo == k else 0
            result += count[(prefix_sum + modulo - k) % modulo]
            count[prefix_sum % modulo] += 1

        return result
