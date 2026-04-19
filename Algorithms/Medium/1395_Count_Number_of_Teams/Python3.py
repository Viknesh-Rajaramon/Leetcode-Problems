from typing import List
from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result, left, right = 0, SortedList(), SortedList(rating[:])
        for r in rating:
            right.remove(r)
            l_s, l_g = left.bisect_left(r), len(left) - left.bisect_right(r)
            r_s, r_g = right.bisect_left(r), len(right) - right.bisect_right(r)
            result += (l_s * r_g) + (l_g * r_s)
            left.add(r)

        return result
