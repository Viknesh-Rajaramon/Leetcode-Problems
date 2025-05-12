from imports import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = deque()
        right = deque()
        n = len(nums)

        for i in range(1, n+1):
            if i == 1:
                left.append(1)
                right.appendleft(1)
            else:
                left.append(left[-1] * nums[i-2])
                right.appendleft(right[0] * nums[n+1-i])
        
        return [a*b for a, b in zip(left, right)]
