from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted(range(n), key = lambda i: intervals[i][0])
        starts, empty = [intervals[i][0] for i in arr], (0, [])
        dp = [[empty] * 5 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            row = dp[i]
            idx = arr[i]
            _, r, w = intervals[idx]
            nxt = bisect_right(starts, r)
            for j in range(1, 5):
                best, sub = dp[i+1][j], dp[nxt][j-1]
                sc = sub[0] + w
                if sc > best[0]:
                    best = (sc, sorted(sub[1] + [idx]))
                elif sc == best[0]:
                    cl = sorted(sub[1] + [idx])
                    if cl < best[1]:
                        best = (sc, cl)
                
                row[j] = best
        
        return dp[0][4][1]
