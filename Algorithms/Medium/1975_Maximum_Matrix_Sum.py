from typing import List
from math import inf

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result, abs_min_val, negative_count = 0, inf, 0
        for row in matrix:
            for val in row:
                abs_val = abs(val)
                result += abs_val
                if val < 0:
                    negative_count += 1
                
                if abs_val < abs_min_val:
                    abs_min_val = abs_val
                
        return result if negative_count % 2 == 0 else result - 2*abs_min_val
