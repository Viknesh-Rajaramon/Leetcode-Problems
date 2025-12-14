from imports import *

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1

        n, idx = len(balance), -1
        for i, b in enumerate(balance):
            if b < 0:
                idx = i
                break

        if idx == -1:
            return 0

        result, need = 0, -balance[idx]
        for d in range(1, n//2 + 1):
            i = (idx + d) % n
            if balance[i] > 0 and need > 0:
                take = min(balance[i], need)
                result += take * d
                need -= take
    
            j = (idx - d) % n
            if i != j and balance[j] > 0 and need > 0:
                take = min(balance[j], need)
                result += take * d
                need -= take
    
            if need == 0:
                return result

        return -1
