from typing import List
from math import inf

class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        result, best_q = None, -inf
        for x, y, q in towers:
            if abs(x - center[0]) + abs(y - center[1]) <= radius:
                if not result or best_q < q:
                    result = [x, y]
                    best_q = q
                elif best_q == q and (x < result[0] or (x == result[0] and y < result[1])):
                        result = [x, y]
                        best_q = q

        return result if result else [-1, -1]
