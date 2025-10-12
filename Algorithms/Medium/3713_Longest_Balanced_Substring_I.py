class Solution:
    def longestBalanced(self, s: str) -> int:
        result, n = 0, len(s)
        for i in range(n):
            freq = {}
            for j in range(i, n):
                if s[j] in freq:
                    freq[s[j]] += 1
                else:
                    freq[s[j]] = 1

                counts = sorted(freq.values())
                if counts[0] == counts[-1]:
                    result = max(result, counts[0] * len(counts))

        return result
