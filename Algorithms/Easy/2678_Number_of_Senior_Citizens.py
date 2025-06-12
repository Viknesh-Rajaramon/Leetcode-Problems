from imports import *

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for p in details if int(p[11 : 13]) > 60)
