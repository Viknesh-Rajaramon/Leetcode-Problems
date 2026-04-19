import string

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        s = s[i : ]

        if s == "":
            return 0
        
        num = ""
        if s[0] == "+" or s[0] == "-":
            num += s[0]
            s = s[1 : ]
        
        for c in s:
            if c in string.digits:
                num += c
            else:
                break
        
        if num == "" or num == "+" or num == "-":
            return 0
        
        return min(max(int(num), -2**31), 2**31 - 1)
