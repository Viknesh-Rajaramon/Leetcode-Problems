class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n, nxt = len(colors), {'R': 'B', 'B': 'W', 'W': 'R'}
        in_degree, degree = [0] * n, [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if nxt[colors[u]] == colors[v]:
                in_degree[v] += 1
            elif nxt[colors[v]] == colors[u]:
                in_degree[u] += 1
            else:
                return -1

        result = -1
        for i in range(n):
            if in_degree[i] > 1:
                return -1

            if in_degree[i] == 0:
                result = i
        
        return result if degree[result] <= 2 else -1
