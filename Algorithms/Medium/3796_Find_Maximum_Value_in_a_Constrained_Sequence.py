from typing import List

class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        result = [0] * n
        for idx, maxVal in restrictions:
            result[idx] = maxVal
        
        for i in range(n-1):
            if not result[i+1] or result[i+1] >= result[i] + diff[i]:
                result[i+1] = result[i] + diff[i]
            else:
                j = i
                while abs(result[j] - result[j+1]) > diff[j]:
                    result[j] = result[j+1] + diff[j]
                    j -= 1

        return max(result)
