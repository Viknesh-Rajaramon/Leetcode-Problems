from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy, available, num_processed = [], [i for i in range(k)], [0] * k
        for i in range(len(arrival)):
            while busy:
                if busy[0][0] <= arrival[i]:
                    _, server = heappop(busy)
                    heappush(available, (i + ((server-i) % k)))
                else:
                    break
            
            if not available:
                continue
            
            virtual_server = heappop(available)
            next_server = virtual_server % k
            num_processed[next_server] += 1
            heappush(busy, (arrival[i] + load[i], next_server))
        
        result, max_reqs = [], max(num_processed)
        for i in range(k):
            if num_processed[i] == max_reqs:
                result.append(i)
        
        return result
