class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        i, j = 0, n-1
        while i < j:
            if s[i] != s[j]:
                str_1 = s[:i] + s[i+1:]
                str_2 = s[:j] + s[j+1:]
                
                return str_1 == str_1[::-1] or str_2 == str_2[::-1]
            
            i += 1
            j -= 1
        
        return True
