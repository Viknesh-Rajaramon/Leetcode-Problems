from typing import List

class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        targetIntervals.sort()
        availableIntervals.sort()
        result, n, i, curr, best = 0, len(availableIntervals), 0, 0, 0
        for s, e in targetIntervals:
            while curr < e:
                t = max(curr, s)
                while i < n and availableIntervals[i][0] <= t:
                    best = max(best, availableIntervals[i][1])
                    i += 1

                if (best < t) or (best == t and t < e):
                    return -1

                curr = best
                result += 1

        return result
