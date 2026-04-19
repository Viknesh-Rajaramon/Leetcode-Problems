class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        n = len(s)

        i, start = 0, ord("a") - 1
        while i < n:
            if i+2 < n and s[i+2] == "#":
                result.append(chr(start + int(s[i:i+2])))
                i += 3
            else:
                result.append(chr(start + int(s[i])))
                i += 1
        
        return "".join(result)
