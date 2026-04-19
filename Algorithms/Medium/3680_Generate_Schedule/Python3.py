from typing import List

class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4:
            return []

        result = []

        taken, first, used = [False] * n, 0, 0
        while used < n:
            if taken[first]:
                first = (first + 1) % n
            else:
                taken[first] = True
                result.append([first, (first + 1) % n])
                used += 1
                first = (first + 2) % n
        
        taken, used = [False] * n, 0
        while used < n:
            if taken[first]:
                first = (first + 1) % n
            else:
                taken[first] = True
                result.append([(first + 1) % n, first])
                used += 1
                first = (first + 2) % n
        
        for d in range(2, n-1):
            while first in result[-1] or ((first + d) % n) in result[-1]:
                first = (first + 1) % n
            
            for _ in range(n):
                result.append([first, (first + d) % n])
                first = (first + 1) % n

        return result
