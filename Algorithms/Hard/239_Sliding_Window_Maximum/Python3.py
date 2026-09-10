from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result, q = [], deque()
        for i, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            
            q.append(num)
            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            
            if i >= k-1:
                result.append(q[0])

        return result
