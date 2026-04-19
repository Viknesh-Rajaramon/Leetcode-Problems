class Solution:
    def lexSmallest(self, s: str) -> str:
        result, rev_s = s, s[::-1]
        for k in range(1, len(s)+1):
            result = min(result, rev_s[-k:] + s[k:], s[:-k] + rev_s[:k])

        return result
