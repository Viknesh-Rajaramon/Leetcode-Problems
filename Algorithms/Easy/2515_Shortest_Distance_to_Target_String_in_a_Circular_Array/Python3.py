from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        result = n = len(words)
        for i in range(n):
            if words[i] == target:
                result = min(result, abs(i-startIndex), n-abs(i-startIndex))
        
        return result if result < n else -1
