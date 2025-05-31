from imports import *

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node: int) -> List[int]:
            queue = deque([(node, 0)])
            visited = set()

            distance = [inf] * len(edges)
            distance[node] = 0

            while queue:
                node, dist = queue.popleft()
                visited.add(node)

                if edges[node] != -1 and edges[node] not in visited:
                    distance[edges[node]] = min(distance[edges[node]], dist+1)
                    queue.append((edges[node], dist+1))
            
            return distance
        
        dist1 = bfs(node1)
        dist2 = bfs(node2)

        result = inf
        index = -1
        for i in range(len(edges)):
            if max(dist1[i], dist2[i]) < result:
                index = i
                result = max(dist1[i], dist2[i])
        
        return index
