from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        result = 0
        
        curr_time = 0
        for i in range(n):
            curr_time += endTime[i] - startTime[i]
            left = 0 if i < k else endTime[i-k]
            right = eventTime if i == n-1 else startTime[i+1]
            result = max(result, right - left - curr_time)
            if i >= k-1:
                curr_time -= endTime[i-k+1] - startTime[i-k+1]

        return result
