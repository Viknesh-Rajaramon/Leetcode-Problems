from math import inf

class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        result, max_light = inf, max(lights)
        for time in arrivalTime:
            r = time % period
            if r >= max_light:
                result = min(result, r)

        return period - result if result != inf else 0
