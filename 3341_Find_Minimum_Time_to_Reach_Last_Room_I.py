from imports import *

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])

        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]
        while heap:
            i, j, time = heappop(heap)
            if i == n-1 and j == m-1:
                return time
            
            if time == dist[i][j]:
                for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ii < n and 0 <= jj < m:
                        new_time = max(time, moveTime[ii][jj]) + 1
                        if dist[ii][jj] > new_time:
                            dist[ii][jj] = new_time
                            heappush(heap, (ii, jj, new_time))
