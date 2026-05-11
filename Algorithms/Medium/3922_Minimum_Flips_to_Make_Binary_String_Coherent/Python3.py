class Solution:
    def minFlips(self, s: str) -> int:
        result = [0, -1]
        for c in s:
            result[int(c)] += 1
        
        if result[0] == 0 or result[1] == -1:
            return 0

        return min(result[0], result[1] - (int(s[0]) and int(s[-1])))
