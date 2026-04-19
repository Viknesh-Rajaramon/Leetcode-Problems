class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)
        
        a, b = s, s
        
        i = 0
        while i < n and s[i] == "9":
            i += 1
        
        if i != n:
            a = s.replace(s[i], "9")

        i = 0
        while i < n and (s[i] == "0" or s[i] == "1"):
            i += 1
        
        if i != n:
            if i == 0:
                b = s.replace(s[i], "1")
            else:
                b = s.replace(s[i], "0")

        return int(a) - int(b)
