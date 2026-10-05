class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        result, n, i = 0, len(intervals), 0
        starts, ends = sorted(x[0] for x in intervals), sorted(x[1] for x in intervals)
        for j in range(n):
            while i < n and ends[i] < starts[j]:
                i += 1

            result += j-i

        return result
