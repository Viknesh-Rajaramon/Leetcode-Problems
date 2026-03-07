from math import inf

class Solution:
    def minFlips(self, s: str) -> int:
        prev, start_0, start_1, start_0_odd, start_1_odd, is_odd = 0, 0, 0, inf, inf, len(s)%2
        for c in s:
            if int(c) == prev:
                if is_odd:
                    start_0_odd = min(start_0_odd, start_1)
                    start_1_odd += 1
                
                start_1 += 1
            else:
                if is_odd:
                    start_1_odd = min(start_1_odd, start_0)
                    start_0_odd += 1
                
                start_0 += 1

            prev ^= 1
        
        return min([start_0, start_1, start_0_odd, start_1_odd])
