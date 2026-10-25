class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        def bits(x: int) -> int:
            res = 0
            while x > 0:
                res += x%2
                x >>= 1
            
            return res
        
        s1, s2 = bits(a), bits(b)
        return s1 * s2 if s1 >= s2 else s2 // s1
