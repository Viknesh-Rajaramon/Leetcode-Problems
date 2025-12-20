from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for s in sentences:
            length = len(s.split(" "))
            maxWords = length if maxWords < length else maxWords
        
        return maxWords
