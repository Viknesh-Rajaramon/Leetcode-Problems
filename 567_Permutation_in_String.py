from imports import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        freq_s1 = Counter(s1)
        for i in range(0, s2_len-s1_len+1):
            freq_s2 = Counter(s2[i : s1_len + i])

            if freq_s1 == freq_s2:
                return True
        
        return False
