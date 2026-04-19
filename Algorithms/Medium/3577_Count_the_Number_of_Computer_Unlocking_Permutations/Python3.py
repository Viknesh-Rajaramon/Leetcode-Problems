from typing import List

MOD, MAX_NUM = 10**9+7, 10**5
FACT = {1: 1}
for i in range(2, MAX_NUM+1):
    FACT[i] = (FACT[i-1] * i) % MOD

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity.count(complexity[0]) > 1 or min(complexity) != complexity[0]:
            return 0
        
        return FACT[len(complexity)-1]
