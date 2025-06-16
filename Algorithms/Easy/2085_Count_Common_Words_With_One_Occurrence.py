from imports import *

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_count, words2_count = Counter(words1), Counter(words2)
        result = 0
        for word, count in words1_count.items():
            if count == 1 and words2_count[word] == 1:
                result += 1
            
        return result
