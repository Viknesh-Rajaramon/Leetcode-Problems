from typing import List
from collections import deque
from math import inf

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        m, n = len(robot), len(factory)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            dp[i][-1] = inf
        
        for j in range(n-1, -1, -1):
            prefix, queue = 0, deque([(m, 0)])
            for i in range(m-1, -1, -1):
                prefix += abs(robot[i] - factory[j][0])
                if queue[0][0] > i+factory[j][1]:
                    queue.popleft()
                
                temp = dp[i][j+1] - prefix
                while queue and queue[-1][1] >= temp:
                    queue.pop()
                
                queue.append((i, temp))
                dp[i][j] = queue[0][1] + prefix
        
        return dp[0][0]
