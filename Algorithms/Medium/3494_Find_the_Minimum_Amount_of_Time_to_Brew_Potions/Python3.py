from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)

        free_time = [0] * n

        for j in range(m):
            now = free_time[0]
            for i in range(1, n):
                now = max(now + skill[i-1]*mana[j], free_time[i])
            
            free_time[n-1] = now + skill[n-1] * mana[j]
            for i in range(n-2, -1, -1):
                free_time[i] = free_time[i+1] - skill[i+1]*mana[j]

        return free_time[-1]
