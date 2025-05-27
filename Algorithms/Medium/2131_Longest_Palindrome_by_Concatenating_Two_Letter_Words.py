from imports import *

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counts = Counter(words)
        
        result, center = 0, False
        for word, count in word_counts.items():
            rev_word = word[::-1]

            if word[0] == word[1]:
                if count % 2:
                    center = True
            
                result += (count // 2) * 4
            elif rev_word in word_counts and word < rev_word:
                result += min(count, word_counts[rev_word]) * 4

        if center:
            result += 2
            
        return result
