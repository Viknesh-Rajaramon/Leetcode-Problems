class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        result = n

        i, num = 0, int(s, 2)
        while i < n and num > k:
            if s[i] == "1":
                num ^= 1 << n-1-i
                result -= 1

            i += 1

        return result
