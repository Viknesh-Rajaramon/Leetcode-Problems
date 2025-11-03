from imports import *

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result, l = 0, 0
        for r in range(1, len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    result += neededTime[l]
                    l = r
                else:
                    result += neededTime[r]
            else:
                l = r

        return result
