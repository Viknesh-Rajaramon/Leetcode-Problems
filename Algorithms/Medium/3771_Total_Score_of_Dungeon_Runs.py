from typing import List
from bisect import bisect_left

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        prefix_damage = [0] * (n+1)
        for i in range(n):
            prefix_damage[i+1] = prefix_damage[i] + damage[i]
        
        result = 0
        for j in range(n):
            required_prefix = requirement[j] + prefix_damage[j+1] - hp
            i = bisect_left(prefix_damage, required_prefix, 0, j+1)
            result += j - i + 1

        return result
