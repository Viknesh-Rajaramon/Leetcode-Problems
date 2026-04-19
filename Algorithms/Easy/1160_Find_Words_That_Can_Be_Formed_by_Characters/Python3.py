from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        chars = Counter(chars)

        for word in words:
            for c in word:
                if word.count(c) > chars[c]:
                    break
            else:
                result += len(word)
        
        return result
