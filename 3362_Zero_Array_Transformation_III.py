from imports import *

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(key = lambda x: x[0])

        heap = []
        diff = [0] * (n+1)
        ops = 0
        j = 0
        for i in range(n):
            ops += diff[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while ops < nums[i] and heap and -heap[0] >= i:
                ops += 1
                diff[-heappop(heap) + 1] -= 1
            
            if ops < nums[i]:
                return -1
        
        return len(heap)
