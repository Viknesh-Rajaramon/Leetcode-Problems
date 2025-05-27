from imports import *

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums)
        total_pairs = n*(n-1) // 2
        
        for i in range(n):
            diff = nums[i] - i
            if diff not in hash_map:
                hash_map[diff] = 0
            
            hash_map[diff] += 1
        
        good_pairs = 0
        for val in hash_map.values():
            good_pairs += val * (val - 1) // 2
        
        return total_pairs - good_pairs
