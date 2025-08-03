from imports import *

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        result, sum_ = 0, 0

        def step(L: int, R: int) -> int:
            return min(R - startPos, startPos - L) + R - L

        left = bisect_left(fruits, [startPos - k, 0])
        right = bisect_right(fruits, [startPos + k + 1, -1])

        l = left
        for r in range(left, right):
            sum_ += fruits[r][1]

            while l <= r and step(fruits[l][0], fruits[r][0]) > k:
                sum_ -= fruits[l][1]
                l += 1
            
            result = max(result, sum_)
        
        return result
