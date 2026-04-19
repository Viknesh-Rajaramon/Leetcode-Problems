class Solution:
    def minLength(self, s: str) -> int:
        s_len = len(s)
        i = 2
        while i < (s_len+1):
            if s[i-2 : i] == "AB" or s[i-2 : i] == "CD":
                s = s[: i-2] + s[i : ]
                i = i-3 if i > 4 else 2
                s_len = len(s)
            else:
                i += 1
        
        return s_len 
