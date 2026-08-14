class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result, l, count = 0, 0, [0] * 26
        for r, c in enumerate(s):
            ch = ord(c) - ord("a")
            count[ch] += 1
            while count[ch] > 2:
                count[ord(s[l]) - ord("a")] -= 1
                l += 1

            result = max(result, r-l+1)

        return result
