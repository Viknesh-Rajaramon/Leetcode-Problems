from imports import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for c in set(words[0]):
            f = min(word.count(c) for word in words)
            result += [c] * f
        
        return result
