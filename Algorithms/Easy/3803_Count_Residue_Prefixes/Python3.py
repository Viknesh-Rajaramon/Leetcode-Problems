class Solution:
    def residuePrefixes(self, s: str) -> int:
        result, chars = 0, set()
        for i, c in enumerate(s):
            chars.add(c)
            if len(chars) == (i+1) % 3:
                result += 1

        return result
