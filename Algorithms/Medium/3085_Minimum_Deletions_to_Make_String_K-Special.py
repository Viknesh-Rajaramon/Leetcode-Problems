from math import inf
from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)
        
        result = inf
        for count_a in counts.values():
            deletions = 0
            for count_b in counts.values():
                if count_a > count_b:
                    deletions += count_b
                elif count_b > count_a + k:
                    deletions += count_b - (count_a + k)
            
            result = min(result, deletions)

        return result
