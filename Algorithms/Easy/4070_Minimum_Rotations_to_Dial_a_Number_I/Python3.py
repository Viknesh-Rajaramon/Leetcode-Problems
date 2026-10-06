class Solution:
    def minRotations(self, s: str) -> int:
        result, curr = 0, 0
        for c in s:
            d = int(c)
            result += min((d-curr+10) % 10, (curr-d+10) % 10)
            curr = d

        return result
