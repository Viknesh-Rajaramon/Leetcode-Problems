from imports import *

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n+4, 4)
