from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences, vFences = sorted([1, m] + hFences), sorted([1, n] + vFences)
        heights = set()
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                heights.add(hFences[j] - hFences[i])

        result = 0
        for i in range(len(vFences)):
            for j in range(len(vFences)-1, i, -1):
                width = vFences[j] - vFences[i]
                if width in heights:
                    result = max(result, width * width)
                    break
        
        return result % (10**9+7) if result else -1
