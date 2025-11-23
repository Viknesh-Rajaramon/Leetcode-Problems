from imports import *

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        rem = total % 3
        if rem == 0:
            return total
        
        h1, h2 = [], []
        for num in nums:
            if num % 3 == 1:
                if len(h1) < 2:
                    heappush(h1, -num)
                elif num < -h1[0]:
                    heapreplace(h1, -num)
            elif num % 3 == 2:
                if len(h2) < 2:
                    heappush(h2, -num)
                elif num < -h2[0]:
                    heapreplace(h2, -num)
        
        r11, r12 = -heappop(h1) if h1 else total, -heappop(h1) if h1 else total
        r21, r22 = -heappop(h2) if h2 else total, -heappop(h2) if h2 else total

        return total - (min(r11, r12, r21+r22) if rem == 1 else min(r21, r22, r11+r12))
