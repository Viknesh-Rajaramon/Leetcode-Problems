from imports import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        intervals.append([inf, inf])
        start, end = intervals[0]

        result = []
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        return result
