from imports import *

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = sorted(Counter(s).items(), key = lambda x: x[1])
        
        result = 0
        for i in range(len(counts)-k):
            result += counts[i][1]

        return result
