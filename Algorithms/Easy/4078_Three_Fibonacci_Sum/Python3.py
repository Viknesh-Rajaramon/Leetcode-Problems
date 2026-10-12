class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        f_0, f_1, f_2 = 0, 1, 1
        while f_0 + f_1 + f_2 <= n:
            if f_0 + f_1 + f_2 == n:
                return True
            
            f_0 = f_1
            f_2 += f_1
            f_1 = f_2 - f_1
        
        return False
