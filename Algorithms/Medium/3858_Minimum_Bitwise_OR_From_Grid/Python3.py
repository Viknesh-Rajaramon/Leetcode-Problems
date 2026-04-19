from typing import List

class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        result = (1<<17) - 1
        for bit in range(16, -1, -1):
            curr = result & ~(1 << bit)
            for row in grid:
                if not any((num | curr) == curr for num in row):
                    break
            else:
                result = curr

        return result
