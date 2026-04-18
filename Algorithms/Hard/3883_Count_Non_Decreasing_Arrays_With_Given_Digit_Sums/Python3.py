from collections import defaultdict

class Solution:
    def countArrays(self, digitSum: list[int]) -> int:
        mod, n = 10**9+7, 5001
        DIGIT_SUMS = defaultdict(set)
        for i in range(n):
            DIGIT_SUMS[sum(map(int, str(i)))].add(i)
        
        result = [1] * n
        for d in digitSum:
            curr = [0] * n
            for i in range(n):
                if i > 0:
                    curr[i] = curr[i-1]
                
                if i in DIGIT_SUMS[d]:
                    curr[i] = (curr[i] + result[i]) % mod
                
            result = curr

        return result[-1]
