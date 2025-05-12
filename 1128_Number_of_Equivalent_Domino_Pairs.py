from imports import *

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        dominoes_map = defaultdict(int)

        for i in range(n):
            dominoes[i].sort()
            dominoes_map[tuple(dominoes[i])] += 1
        
        result = 0
        for val in dominoes_map.values():
            result += (val * (val - 1)) // 2

        return result
