from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}
        for s in strs:
            zeroes, ones, new_dp = s.count("0"), s.count("1"), dict(dp)
            for (prev_zeroes, prev_ones), val in dp.items():
                new_zeroes, new_ones = prev_zeroes + zeroes, prev_ones + ones
                if new_zeroes <= m and new_ones <= n:
                    new_dp[(new_zeroes, new_ones)] = max(new_dp.get((new_zeroes, new_ones), 0), val + 1)

            dp = new_dp
        
        return max(dp.values())
