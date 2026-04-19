from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        left = [0] * n
        left[0] = startTime[0]
        for i in range(1, n):
            left[i] = max(left[i-1], startTime[i] - endTime[i-1])

        right = [0] * n
        right[n-1] = eventTime - endTime[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], startTime[i+1] - endTime[i])

        result = 0
        for i in range(n):
            l = left[i] if i == 0 else startTime[i] - endTime[i-1]
            r = right[i] if i == n-1 else startTime[i+1] - endTime[i]

            diff = endTime[i] - startTime[i]
            if (i != 0 and left[i-1] >= diff) or (i != n-1 and right[i+1] >= diff):
                result = max(result, l + r + diff)
            else:
                result = max(result, l + r)
        
        return result
