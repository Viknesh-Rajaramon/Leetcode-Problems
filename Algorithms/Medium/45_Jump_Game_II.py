from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        steps, jumps, end = 0, 0, 0
        for i in range(n-1):
            steps = max(steps, i + nums[i])

            if i == end:
                jumps += 1
                end = steps
            
        return jumps
