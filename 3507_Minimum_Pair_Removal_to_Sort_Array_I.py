from imports import *

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        ops = 0    
        while True:
            if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
                return ops
    
            min_sum = inf
            min_idx = -1
            for i in range(len(nums)-1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_idx = i
    
            merged = nums[min_idx] + nums[min_idx + 1]
            nums = nums[:min_idx] + [merged] + nums[min_idx + 2:]
            ops += 1
