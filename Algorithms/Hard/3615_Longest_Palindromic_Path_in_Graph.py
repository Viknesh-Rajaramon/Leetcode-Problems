from imports import *

class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        edges.sort()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        if len(edges) == (n * (n-1)) // 2:
            count = Counter(label)
            mid = any(x%2 for x in count.values())
            return sum((x//2) * 2 for x in count.values()) + mid
        
        @lru_cache(None)
        def dfs(i: int, j: int, mask: int) -> int:
            ans = mask.bit_count()
            s1 = [x for x in graph[i] if not mask & (1 << x)]
            s2 = [x for x in graph[j] if not mask & (1 << x)]

            for a, b in product(s1, s2):
                u, v = min(a, b), max(a, b)
                if u != v and label[u] == label[v]:
                    ans = max(ans, dfs(u, v, mask | 1 << u | 1 << v))

            return ans
        
        ans1 = max(dfs(i, i, 1<<i) for i in range(n))
        ans2 = max([dfs(i, j, 1<<i | 1<<j) for i, j in edges if label[i] == label[j]], default = 0)
        return max(ans1, ans2)
