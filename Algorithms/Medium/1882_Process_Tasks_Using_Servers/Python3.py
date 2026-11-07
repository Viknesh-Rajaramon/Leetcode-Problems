from heapq import heapify, heappop, heappush

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        result, busy, idle = [], [], [(w, i, 0) for i, w in enumerate(servers)]
        heapify(idle)
        for i, task in enumerate(tasks):
            while busy and busy[0][0] <= i:
                t, w, idx = heappop(busy)
                heappush(idle, (w, idx, t))
            
            if idle:
                w, idx, t = heappop(idle)
                result.append(idx)
                heappush(busy, (i+task, w, idx))
            else:
                t, w, idx = heappop(busy)
                result.append(idx)
                heappush(busy, (t+task, w, idx))

        return result
