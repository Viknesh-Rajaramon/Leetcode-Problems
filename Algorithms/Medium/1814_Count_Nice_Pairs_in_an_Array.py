from imports import *

class Solution:
    def rev(self, num: int) -> int:
        return int(str(num)[::-1])
    
    def countNicePairs(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums)
        mod = 10**9+7
        
        for i in range(n):
            diff = nums[i] - self.rev(nums[i])
            if diff not in hash_map:
                hash_map[diff] = 0
            
            hash_map[diff] += 1
        
        nice_pairs = 0
        for val in hash_map.values():
            nice_pairs = (nice_pairs + (val * (val - 1) // 2) % mod) % mod
        
        return nice_pairs
