from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or len(weights) == k:
            return 0
        
        n = len(weights)
        pair_weights = [weights[i]+weights[i+1] for i in range(n-1)]

        pair_weights.sort()
        return sum(pair_weights[n-k:]) - sum(pair_weights[:k-1])
