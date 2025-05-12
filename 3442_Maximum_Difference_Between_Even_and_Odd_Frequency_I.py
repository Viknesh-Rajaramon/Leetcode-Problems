from imports import *

class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = [0] * 26
        for i in range(26):
            freq_map[i] = 0
        
        n = len(s)
        for i in range(n):
            freq_map[ord(s[i])-ord("a")] += 1
        
        max_odd = 0
        min_even = inf
        for val in freq_map:
            if val == 0:
                continue
            
            if val % 2 == 0:
                min_even = val if val < min_even else min_even
            else:
                max_odd = val if val > max_odd else max_odd

        return max_odd - min_even
