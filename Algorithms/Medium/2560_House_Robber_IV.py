from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def canSteal(guess: int) -> bool:
            i = 0
            count = 0
            while i < n:
                if nums[i] <= guess:
                    count += 1
                    i += 2
                else:
                    i += 1
            
            return count >= k
        
        l, r = min(nums), max(nums)

        while l <= r:
            m = (l+r) // 2
            if canSteal(m):
                ans = m
                r = m-1
            else:
                l = m+1
        
        return l
