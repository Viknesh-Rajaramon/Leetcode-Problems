from imports import *

class Solution:
    def factorial(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        
        return fact

    def nCk(self, n: int, k: int) -> int:
        return self.factorial(n) // (self.factorial(n-k) * self.factorial(k))

    def getRow(self, rowIndex: int) -> List[int]:
        arr = []
        for i in range(0, rowIndex+1):
            arr.append(self.nCk(rowIndex, i))
        
        return arr
