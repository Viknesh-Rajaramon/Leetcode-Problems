class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def f(c: str) -> int:
            return ord(c) - ord('0')
        
        def diff(i: int) -> int:
            return 10*(f(endTime[i]) - f(startTime[i])) + f(endTime[i+1]) - f(startTime[i+1])
        
        return 60*(60*(diff(0)) + diff(3)) + diff(6)
