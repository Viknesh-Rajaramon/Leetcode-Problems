from imports import *

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        return sum(abs(s[c] - t[c]) for c in string.ascii_lowercase) // 2
