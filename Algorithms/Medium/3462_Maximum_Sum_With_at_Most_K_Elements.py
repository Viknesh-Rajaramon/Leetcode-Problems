from imports import *

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        heap = []

        for i in range(n):
            for j in range(m):
                heap.append((-grid[i][j], i))

        heapify(heap)
        
        sum = 0
        count = 0
        while count < k:
            num, row = heappop(heap)
            if limits[row] > 0:
                limits[row] -= 1
                sum += num
                count += 1

        return sum * -1
