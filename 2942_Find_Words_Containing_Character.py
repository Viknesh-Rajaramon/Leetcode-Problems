from imports import *

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(0, len(words)):
            if words[i].find(x) != -1:
                arr.append(i)
        
        return arr
