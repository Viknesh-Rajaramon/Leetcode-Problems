class Solution:
    def numTrees(self, n: int) -> int:
        numerator = 1
        for i in range(n+2, 2*n+1):
            numerator *= i
        
        denominator = 1
        for i in range(2, n+1):
            denominator *= i
        
        return numerator // denominator
