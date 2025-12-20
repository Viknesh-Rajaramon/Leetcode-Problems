from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z_cnt = s.count("0")
        if z_cnt == 0:
            return 0
        
        if k%2 == 0 and z_cnt%2 == 1:
            return -1

        n = len(s)
        last = [n-1, n] if n%2 == 1 else [n, n-1]
        nxt = [{}, {}]

        def find(p: int, x: int) -> int:
            if x > last[p]:
                return x
            
            r = nxt[p].get(x, x)
            if r != x:
                r = find(p, r)
                nxt[p][x] = r
            
            return r
        
        dist = [-1] * (n+1)
        dist[z_cnt] = 0

        queue = deque([z_cnt])
        while queue:
            u = queue.popleft()
            if u == 0:
                return dist[0]
            
            i_min, i_max = max(0, k - n + u), min(k, u)
            if i_min > i_max:
                continue
            
            p = (u+k) & 1
            x = u+k-2*i_max if (u+k-2*i_max&1) == p else u+k-2*i_max+1
            while True:
                v = find(p, x)
                if v > u+k-2*i_min:
                    break
                
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
                
                nxt[p][v] = find(p, v+2)
                x = v+2

        return -1
