from imports import *

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_time, min_index = 0, inf
        last_press_time = 0
        
        for i in range(len(events)):
            diff = events[i][1] - last_press_time
            last_press_time = events[i][1]

            if diff > longest_time:
                longest_time = diff
                min_index = events[i][0]
            elif diff == longest_time:
                min_index = min(min_index, events[i][0])
        
        return min_index
