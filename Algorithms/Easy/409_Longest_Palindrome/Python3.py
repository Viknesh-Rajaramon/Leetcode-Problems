from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        mid = False
        counts = sorted(Counter(s).values(), reverse = True)
        max_length = 0
        for c in counts:
            if c % 2:
                if mid:
                    max_length += c-1
                else:
                    max_length += c
                    mid = True
            else:
                max_length += c
        
        return max_length
