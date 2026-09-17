from typing import List
from math import inf
from heapq import heappop, heappush

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        moves = [(0, 1, 0), (1, 0, 0), (0, -1, 1), (-1, 0, 1)]
        dist = [[[inf, inf] for _ in range(n)] for _ in range(m)]
        dist[0][0][0], heap = 1, [(1, 0, 0, 0)]
        while heap:
            cost, i, j, parity = heappop(heap)
            if cost != dist[i][j][parity]:
                continue
            
            if i == m-1 and j == n-1:
                return cost
            
            new_cost, new_parity = cost + penalty[i][j], 1 ^ parity
            if new_cost < dist[i][j][new_parity]:
                dist[i][j][new_parity] = new_cost
                heappush(heap, (new_cost, i, j, new_parity))
            
            for di, dj, allowed_parity in moves:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                
                move_cost = (ni+1)*(nj+1) + (0 if parity == allowed_parity else penalty[i][j])
                new_cost, new_parity = cost + move_cost, 1 ^ parity
                if new_cost < dist[ni][nj][new_parity]:
                    dist[ni][nj][new_parity] = new_cost
                    heappush(heap, (new_cost, ni, nj, new_parity))
        
        return -1
