from imports import *

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        color_count = [defaultdict(int) for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        max_color_value = 0
        while queue:
            u = queue.popleft()

            color_count[u][colors[u]] += 1
            max_color_value = max(max_color_value, color_count[u][colors[u]])

            for v in graph[u]:
                for color, count in color_count[u].items():
                    color_count[v][color] = max(count, color_count[v][color])
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        for i in range(n):
            if indegree[i] != 0:
                return -1

        return max_color_value
