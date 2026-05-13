from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n, diff = len(nums), [0] * (2*limit+2)
        for i in range(n//2):
            a, b = min(nums[i], nums[n-1-i]), max(nums[i], nums[n-1-i])
            diff[2] += 2
            diff[a+1] -= 1
            diff[a+b] -= 1
            diff[a+b+1] += 1
            diff[b+limit+1] += 1
        
        result, curr_ops = n, 0
        for i in range(2, 2*limit+1):
            curr_ops += diff[i]
            result = min(result, curr_ops)

        return result
