from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq_1, freq_2, moves = Counter(basket1), Counter(basket2), []
        for fruit in set(freq_1) | set(freq_2):
            if (freq_1[fruit] + freq_2[fruit]) % 2 != 0:
                return -1
            
            f = abs(freq_1[fruit] - freq_2[fruit]) // 2
            if f:
                moves.extend([fruit] * f)
        
        if not moves:
            return 0
        
        moves.sort()
        result, min_ = 0, min(basket1 + basket2)
        for i in range(len(moves) // 2):
            result += min(2 * min_, moves[i])

        return result
