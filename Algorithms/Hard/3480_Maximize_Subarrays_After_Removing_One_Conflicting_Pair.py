from imports import *

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        n += 1
        conflictingPairs.sort(key = lambda p: max(p))
        conflictingPairs.append([n, n])

        max_diff, max_left, remain = 0, 0, 0
        max_second_left, second_remain = 0, 0
        for left, right in conflictingPairs:
            if left > right:
                left, right = right, left
            
            if left > max_left:
                max_diff = max(max_diff, (max_second_left - max_left) * (n - right) + remain - second_remain)
                second_remain = remain
                remain += (left - max_left) * (n - right)
                max_left, max_second_left = left, max_left
            elif left > max_second_left:
                second_remain += (left - max_second_left) * (n - right)
                max_second_left = left
        
        return n * (n - 1) // 2 - remain + max_diff
