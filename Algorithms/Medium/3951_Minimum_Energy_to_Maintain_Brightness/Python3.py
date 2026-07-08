class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()
        time = 0
        start, end = intervals[0]
        for s, e in intervals[1 : ]:
            if s <= end+1:
                end = max(end, e)
            else:
                time += end-start+1
                start, end = s, e
        
        time += end-start+1
        return time * ((brightness+2) // 3)
