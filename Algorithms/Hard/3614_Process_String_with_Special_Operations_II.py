class Solution:
    def processStr(self, s: str, k: int) -> str:
        str_len = 0
        for c in s:
            if c == "*":
                if str_len > 0:
                    str_len -= 1
            elif c == "%":
                pass
            elif c == "#":
                str_len *= 2
            else: 
                str_len += 1
        
        if k >= str_len:
            return "."
        
        for c in reversed(s):
            if c == "*":
                str_len += 1
            elif c == "%":
                k = str_len - k - 1
            elif c == "#":
                str_len //= 2
                if k >= str_len:
                    k -= str_len
            else: 
                str_len -= 1
                if k == str_len:
                    return c
