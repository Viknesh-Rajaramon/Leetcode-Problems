from imports import *

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        n, m = len(fruits), len(baskets)
        for i in range(n):
            for j in range(m):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    result += 1
                    break
        
        return n - result
