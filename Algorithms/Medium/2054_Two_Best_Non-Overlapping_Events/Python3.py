from typing import List
from math import inf
from collections import deque

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ends = deque(sorted(events, key = lambda x: x[1]))

        result, end_max = max(map(lambda x: x[2], events)), -inf
        for start, _, value in sorted(events, key = lambda x: x[0]):
            while ends and ends[0][1] < start:
                end_max = max(end_max, ends.popleft()[2])
            
            result = max(result, value + end_max)

        return result
