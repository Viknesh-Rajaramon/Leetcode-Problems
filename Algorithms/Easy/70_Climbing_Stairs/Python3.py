class Solution:
    def factorial(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        
        return fact
    
    def nCk(self, n:int, k:int) -> int:
        return self.factorial(n) // (self.factorial(n-k) * self.factorial(k))

    def climbStairs(self, n: int) -> int:
        upperLimit = n//2
        sum = 0
        for k in range(0, upperLimit+1):
            sum += self.nCk(n-k, k)
        return sum
