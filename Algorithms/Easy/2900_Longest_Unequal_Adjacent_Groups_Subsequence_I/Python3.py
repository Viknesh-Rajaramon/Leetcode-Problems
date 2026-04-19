from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        
        result = [words[0]]
        group = groups[0]
        for i in range(1, n):
            if groups[i] != group:
                result.append(words[i])
                group = groups[i]
        
        return result
