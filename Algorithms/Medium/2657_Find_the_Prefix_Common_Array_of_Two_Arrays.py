from imports import *

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result, freq = [], [0] * n
        curr = 0
        for i in range(n):
            freq[A[i] - 1] += 1
            freq[B[i] - 1] += 1
            
            if freq[A[i] - 1] == 2:
                curr += 1

            if A[i] != B[i] and freq[B[i] - 1] == 2:
                curr += 1

            result.append(curr)

        return result
