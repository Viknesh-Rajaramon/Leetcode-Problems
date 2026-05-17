class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def count(n: int) -> int:
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            if k == 1:
                return n+1
            
            x = int(n**(1.0/k))
            while (x+1)**k <= n:
                x += 1
            
            while x**k > n:
                x -= 1
            
            return x+1

        return count(r) - count(l-1)
