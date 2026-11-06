from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x: x[1])
        ids = sorted(range(len(queries)), key = lambda i: queries[i])
        result, count, l, r, active = [0] * len(queries), [0] * (n+1), 0, 0, 0
        for i in ids:
            while r < len(logs) and logs[r][1] <= queries[i]:
                server = logs[r][0]
                if count[server] == 0:
                    active += 1
                
                count[server] += 1
                r += 1
            
            temp = queries[i]-x
            while l < r and logs[l][1] < temp:
                server = logs[l][0]
                count[server] -= 1
                if count[server] == 0:
                    active -= 1
                
                l += 1

            result[i] = n-active

        return result
