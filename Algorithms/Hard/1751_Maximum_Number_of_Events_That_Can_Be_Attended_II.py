from imports import *

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        
        def binary_search(low: int, high: int) -> int:
            i = low - 1
            while low < high:
                mid = (low + high) // 2
                if events[mid][0] > events[i][1]:
                    high = mid
                else:
                    low = mid + 1
            
            return low
        
        nxt, prev = [binary_search(i+1, n) for i in range(n)], [0] * (n + 1)
        for _ in range(k):
            curr = [0] * (n + 1)
            for i in range(n-1, -1, -1):
                curr[i] = max(curr[i+1], events[i][2] + (prev[nxt[i]] if nxt[i] < n else 0))
            
            prev = curr
        
        return prev[0]
