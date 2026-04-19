class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result, chars = 0, set(s)
        for c in chars:
            first = s.find(c)
            last = s.rfind(c)

            if first != last:
                result += len(set(s[first+1 : last]))
            
        return result
