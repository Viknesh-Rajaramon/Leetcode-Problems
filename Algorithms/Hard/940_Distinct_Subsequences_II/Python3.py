class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp, last, mod = 1, {}, 10**9 + 7
        for c in s:
            new_dp = dp*2
            if c in last:
                new_dp -= last[c]

            last[c], dp = dp, new_dp % mod

        return (dp-1) % mod
