from imports import *

class Solution:
    def pivotInteger(self, n: int) -> int:
        temp = n * (n+1) // 2
        x = int(sqrt(temp))
        return x if x*x == temp else -1
