from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        curr_sum = 0

        hash_map = defaultdict(int)
        hash_map[0] = 1

        for i in range(n):
            curr_sum += nums[i]
            result += hash_map[curr_sum-k]
            hash_map[curr_sum] = 1 + hash_map[curr_sum]
        
        return result
