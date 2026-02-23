from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return "".join(chr(122 - sum(weights[ord(c)-97] for c in word) % 26) for word in words)
