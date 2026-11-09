from math import gcd

class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        m, n = len(a), len(b)
        ta, tb = m * x, n * y
        if tb > ta:
            return False
            
        temp = min(tb, (m * n) // gcd(m, n))
        for i in range(m):
            if i + tb > ta:
                break
                
            ok = True
            for j in range(temp):
                if b[j % n] != a[(i+j) % m]:
                    ok = False
                    break
                    
            if ok:
                return True
                
        return False
