from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for word in words if word[:min(len(pref), len(word))] == pref)
