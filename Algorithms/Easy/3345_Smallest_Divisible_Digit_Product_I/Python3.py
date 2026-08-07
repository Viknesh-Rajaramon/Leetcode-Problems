class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+10):
            tmp = 1
            for j in list(str(i)):
                tmp *= int(j)
            
            if tmp % t == 0:
                return i
