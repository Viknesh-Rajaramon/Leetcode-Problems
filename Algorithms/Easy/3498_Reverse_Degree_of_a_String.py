class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        z_ord = ord("z")
        for i, c in enumerate(s):
            result += (i+1) * (z_ord + 1 - ord(c))
        
        return result
