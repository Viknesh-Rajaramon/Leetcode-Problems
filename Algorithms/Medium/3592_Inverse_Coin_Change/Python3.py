from typing import List

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        numWays = [1] + numWays
        
        result = []
        for i in range(1, n+1):
            if numWays[i] > 1:
                return []
            
            if numWays[i] == 0:
                continue
            
            result.append(i)
            for j in range(n, i-1, -1):
                numWays[j] -= numWays[j-i]
                if numWays[j] < 0:
                    return []
                
        return result
