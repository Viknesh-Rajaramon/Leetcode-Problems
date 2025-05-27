from imports import *

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        pq = PriorityQueue()

        for i in range(n):
            pq.put((nums[i], i))
        
        for _ in range(k):
            x, index = pq.get()
            pq.put((x * multiplier, index))
        
        ans = [-1] * n
        for _ in range(n):
            x, index = pq.get()
            ans[index] = x
        
        return ans
