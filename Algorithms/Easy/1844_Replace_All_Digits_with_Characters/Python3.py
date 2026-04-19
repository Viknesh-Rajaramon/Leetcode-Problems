class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, i: int) -> str:
            return chr(ord(c) + i)

        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            else:
                result.append(shift(result[-1], int(c)))
        
        return "".join(result)
