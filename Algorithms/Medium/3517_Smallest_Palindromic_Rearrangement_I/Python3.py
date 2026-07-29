from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        result, n = [], len(s)
        mid, counter = "" if n%2 == 0 else s[n//2], Counter(s[ : n//2])
        for i in range(26):
            c = chr(ord('a') + i)
            result.extend([c] * counter[c])
        
        result.append(mid)
        for i in range(25, -1, -1):
            c = chr(ord('a') + i)
            result.extend([c] * counter[c])
        
        return "".join(result)
