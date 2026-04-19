from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordering = defaultdict(lambda: 27)
        i = 1
        for c in order:
            ordering[c] = i
            i += 1
        
        return "".join(sorted(s, key = lambda x: ordering[x]))
