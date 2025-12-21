from typing import List

class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n, delta = len(technique1), [t1- t2 for t1, t2 in zip(technique1, technique2)]
        idx = sorted(range(n), key = lambda x: delta[x], reverse = True)

        result, used = 0, [False] * n
        for i in range(k):
            result += technique1[idx[i]]
            used[idx[i]] = True
        
        for i in range(n):
            if not used[i]:
                result += max(technique1[i], technique2[i])

        return result
