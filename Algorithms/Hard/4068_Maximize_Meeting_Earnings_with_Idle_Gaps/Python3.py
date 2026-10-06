from math import inf
from bisect import bisect_right

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key = lambda x: x[1])
        result, ends, best = 0, [-1], [-inf]
        for start, end, revenue in meetings:
            pos = bisect_right(ends, start)
            prev = start + best[pos-1]
            if prev > 0:
                revenue += prev
            
            result = max(result, revenue)
            if revenue - end > best[-1]:
                ends.append(end)
                best.append(revenue-end)

        return result
