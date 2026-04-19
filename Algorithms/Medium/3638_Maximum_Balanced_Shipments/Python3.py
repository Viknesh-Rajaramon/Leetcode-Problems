from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        max_weight = 0
        result = 0
        for w in weight:
            if w < max_weight:
                result += 1
                max_weight = 0
            else:
                max_weight = w

        return result
