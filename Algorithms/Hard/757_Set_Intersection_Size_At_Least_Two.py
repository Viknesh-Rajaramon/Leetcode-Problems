from typing import List
from math import inf

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))
        result, prev_start, prev_end = 0, -inf, -inf
        for start, end in intervals:
            if start > prev_end:
                result += 2
                prev_start, prev_end = end-1, end
            elif start > prev_start:
                result += 1
                prev_start, prev_end = prev_end, end

        return result
