from imports import *

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        if complexity.count(complexity[0]) > 1 or min(complexity) != complexity[0]:
            return 0
        
        fact = 1
        for i in range(2, len(complexity)):
            fact = (fact * i) % mod

        return fact
