class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return False

        replaced, rch, i, j = False, '', 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            else:
                if not replaced:
                    replaced, rch = True, s[i]
                    i += 1
                else:
                    if rch == t[j]:
                        replaced = False
                    
            j += 1
    
        return i == m
