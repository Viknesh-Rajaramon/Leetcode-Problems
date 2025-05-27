from imports import *

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 1, 0, 0)]
        while heap:
            time, step, i, j = heappop(heap)
            if i == n-1 and j == m-1:
                return time
            
            if time == dist[i][j]:
                new_step = 3 - step
                for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ii < n and 0 <= jj < m:
                        new_time = max(time, moveTime[ii][jj]) + step
                        if dist[ii][jj] > new_time:
                            dist[ii][jj] = new_time
                            heappush(heap, (new_time, new_step, ii, jj))
