from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        if all(x == 0 for x in nums):
            return 0

        def canZero(k: int) -> bool:
            diff = [0] * (n+1)
            for i in range(k):
                l_i, r_i, val_i = queries[i]
                diff[l_i] += val_i
                if r_i+1 < n+1:
                    diff[r_i+1] -= val_i

            curr_sum = 0
            for i in range(n):
                curr_sum += diff[i]
                if curr_sum < nums[i]:
                    return False
            
            return True
        
        l, r = 1, len(queries)
        ans = -1
        while l <= r:
            m = (l+r) // 2
            if canZero(m):
                ans = m
                r = m-1
            else:
                l = m+1

        return ans
