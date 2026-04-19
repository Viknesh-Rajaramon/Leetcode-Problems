from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0

        for f in fruits:
            for b in baskets:
                if b >= f:
                    baskets.remove(b)
                    result += 1
                    break
        
        return len(fruits) - result
