from imports import *

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        if n == 2:
            return values[0] + values[1] - 1
        
        suffix = [0] * n
        suffix[n-1] = values[n-1] - (n-1)

        for j in range(n-2, -1, -1):
            suffix[j] = max(suffix[j+1], values[j] - j)
        
        max_score = -inf
        for i in range(n-1):
            max_score = max(max_score, values[i] + i + suffix[i+1])
        
        return max_score
