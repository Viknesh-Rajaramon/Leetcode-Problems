class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s, idx_t = 0, 0

        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1

            idx_t += 1

        if idx_s == len(s):
            return True
        
        return False
