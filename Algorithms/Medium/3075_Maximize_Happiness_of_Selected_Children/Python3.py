from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        result = 0
        for i in range(k):
            gain = happiness[i] - i
            if gain <= 0:
                return result
            
            result += gain

        return result
