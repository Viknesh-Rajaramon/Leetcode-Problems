from imports import *

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7

        y_to_x = defaultdict(list)
        for x, y in points:
            y_to_x[y].append(x)

        segment_counts = []
        for y, x_list in y_to_x.items():
            count = len(x_list)
            if count >= 2:
                segment_counts.append(count * (count - 1) // 2)

        total_sum = sum(segment_counts)
        total_sq_sum = sum(c * c for c in segment_counts)
        result = (total_sum * total_sum - total_sq_sum) // 2

        return result % mod
