from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        exp_sum_4 = [1] + [0] * 17
        def exp_sum(x: int) -> int:
            if x == 0:
                return 0
            
            log_4 = (x.bit_length() - 1) >> 1
            r = x - (1 << (log_4 << 1))
            return exp_sum_4[log_4] + r * (log_4+1)
        
        for i in range(17):
            exp_sum_4[i+1] = exp_sum_4[i] + 3 * (i+1) * (1 << (2*i)) + 1

        result = 0
        for l, r in queries:
            result += (exp_sum(r) - exp_sum(l-1) + 1) >> 1

        return result
