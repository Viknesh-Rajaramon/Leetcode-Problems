from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        result, n = 0, len(matrix[0])
        heights = [0] * n
        for row in matrix:
            for c in range(n):
                heights[c] = heights[c] + 1 if row[c] else 0
            
            curr_row = sorted(heights, reverse = True)
            for i in range(n):
                result = max(result, curr_row[i]*(i+1))

        return result
