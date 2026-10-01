class Solution:
    def countRotations(self, s: str, k: int) -> int:
        result = 1 if s[0] == s[-1] else 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                result += 1

        if k == result:
            return len(s) - result

        return result if k == result-1 else 0
