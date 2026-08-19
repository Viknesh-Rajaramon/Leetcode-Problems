from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                rows[row] |= 1 << (seat-2)
            
        result, left, middle, right = 2*(n - len(rows)), 0b00001111, 0b00111100, 0b11110000
        for mask in rows.values():
            if mask & left == 0 or mask & middle == 0 or mask & right == 0:
                result += 1

        return result
