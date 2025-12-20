from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return sum(1 for word in words if word != word[::-1] and word[::-1] in words) // 2
