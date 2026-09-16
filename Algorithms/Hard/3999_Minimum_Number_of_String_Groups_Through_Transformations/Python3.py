from typing import List

class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        def duval(s: str) -> str:
            n = len(s)
            if n <= 1:
                return s
            
            i, j, k = 0, 1, 0
            while i < n and j < n and k < n:
                cik, cjk = s[(i+k)%n], s[(j+k)%n]
                if cik == cjk:
                    k += 1
                elif cik < cjk:
                    j += k+1
                    k = 0
                else:
                    i = max(i+k+1, j)
                    j = i+1
                    k = 0

            ans = min(i, j) % n
            return s[ans : ] + s[ : ans]
        
        return len({duval(w[ : : 2]) + duval(w[1 : : 2]) for w in words})
