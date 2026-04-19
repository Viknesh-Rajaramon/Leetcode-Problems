from math import inf

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        result, min_capacity = -1, inf
        for i, cap in enumerate(capacity):
            if cap >= itemSize and cap < min_capacity:
                result, min_capacity = i, cap

        return result
