from typing import List
from collections import defaultdict

class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        result, counts = 0, defaultdict(int)
        for word in words:
            if len(word) < k:
                continue
            
            counts[word[ : k]] += 1
            if counts[word[ : k]] == 2:
                result += 1

        return result
