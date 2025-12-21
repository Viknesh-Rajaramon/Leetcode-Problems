from typing import List

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        total_sum = n*(n+1) // 2
        if total_sum < abs(target):
            return []
        
        diff = total_sum - target
        if diff % 2:
            return []
        
        diff //= 2
        result, i = list(range(1, n+1)), n-1
        while i >= 0 and diff != 0:
            if diff >= result[i]:
                diff -= result[i]
                result[i] = -result[i]

            i -= 1

        result.sort()
        return result
