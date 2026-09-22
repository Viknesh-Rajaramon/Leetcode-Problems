from math import inf
from bisect import bisect_left

class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        if start not in requests:
            requests.append(start)

        requests.sort()
        m = len(requests)
        dp_0, dp_1 = [[inf] * m for _ in range(m)], [[inf] * m for _ in range(m)]
        start = bisect_left(requests, start)
        dp_0[start][start], dp_1[start][start] = 0, 0
        for l in range(1, m):
            rem = m-l
            for i in range(m-l+1):
                j = i+l-1
                if i:
                    dp_0[i-1][j] = min(
                        dp_0[i-1][j],
                        dp_0[i][j] + (requests[i]-requests[i-1])*rem,
                        dp_1[i][j] + (requests[j]-requests[i-1])*rem
                    )

                if j < m - 1:
                    dp_1[i][j+1] = min(
                        dp_1[i][j+1],
                        dp_0[i][j] + (requests[j+1]-requests[i])*rem,
                        dp_1[i][j] + (requests[j+1]-requests[j])*rem
                    )

        return min(dp_0[0][m-1], dp_1[0][m-1])
