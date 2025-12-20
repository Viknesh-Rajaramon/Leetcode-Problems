from typing import List

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def factorial() -> List[int]:
            f = [1]
            for i in range(1, n+1):
                f.append(f[-1] * i)
            
            return f

        s = set()
        base = 10**((n-1) // 2)
        skip = n & 1

        for i in range(base, 10*base):
            num_str = str(i)
            num_str = num_str + num_str[::-1][skip:]
            
            if int(num_str) % k == 0:
                s.add("".join(sorted(num_str)))
            
        f = factorial()
        ans = 0
        for num in s:
            count = [0] * 10
            for c in num:
                count[int(c)] += 1
            
            total = (n-count[0]) * f[n-1]
            for x in count:
                total //= f[x]
            
            ans += total
        
        return ans
