from imports import *

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        row_sums = [sum(grid[i]) for i in range(m)]
        col_sums = [sum(i) for i in zip(*grid)]
        total_sum = sum(row_sums)

        if total_sum % 2:
            return False

        half_sum = total_sum // 2
        curr_sum = 0
        for i in range(m):
            curr_sum += row_sums[i]
            if curr_sum == half_sum:
                return True

        curr_sum = 0
        for i in range(n):
            curr_sum += col_sums[i]
            if curr_sum == half_sum:
                return True

        return False
