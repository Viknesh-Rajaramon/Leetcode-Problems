from math import comb

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        result = 0
        for bit in range(50, -1, -1):
            count = comb(bit, k)
            if n > count:
                n -= count
                result |= (1 << bit)
                k -= 1

                if k == 0:
                    break

        return result
