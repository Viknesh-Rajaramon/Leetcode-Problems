from math import comb

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1 if n >= 1 else 0
        
        B = n.bit_length()
        depth = [-1] + [0] * B
        for d in range(2, B+1):
            depth[d] = 1 + depth[d.bit_count()]
        
        S = [d for d in range(1, B+1) if depth[d] == k-1]
        if not S:
            return 0

        def count_ones_upto(n: int, c: int) -> int:
            result, used = 0, 0

            for i in reversed(range(n.bit_length())):
                if n >> i & 1:
                    needed = c - used
                    if 0 <= needed <= i:
                        result += comb(i, needed)
                    
                    used += 1
                    if used > c:
                        break
            else:
                if used == c:
                    result += 1
            
            return result
        
        result = 0
        for c in S:
            result += count_ones_upto(n, c)
        
        if 1 in S and n >= 1:
            result -= 1

        return result
