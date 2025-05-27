from imports import *

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        n = len(nums)
        
        for i in range(n-k+1):
            for num in set(nums[i:i+k]):
                hash_map[num] += 1

        max_val = -1

        for key, val in hash_map.items():
            if val == 1:
                max_val = max(max_val, key)

        return max_val
