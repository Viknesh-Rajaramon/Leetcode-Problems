from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_sum, double_sum = 0, 0
        for n in nums:
            if n < 10:
                single_sum += n
            else:
                double_sum += n
        
        return single_sum != double_sum
