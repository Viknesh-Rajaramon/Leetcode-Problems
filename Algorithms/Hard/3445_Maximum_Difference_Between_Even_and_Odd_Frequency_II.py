from imports import *

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        result = -inf

        for a in "01234":
            for b in "01234":
                if a == b:
                    continue
                
                count_a = [0] * (n+1)
                count_b = [0] * (n+1)

                for i in range(n):
                    count_a[i+1] = count_a[i] + (s[i] == a)
                    count_b[i+1] = count_b[i] + (s[i] == b)
                
                best_diff = [[-inf] * 2 for _ in range(2)]
                l = 1
                
                for r in range(k, n+1):
                    while r-l+1 >= k and count_a[r] > count_a[l-1] and count_b[r] > count_b[l-1]:
                        pa = count_a[l-1] % 2
                        pb = count_b[l-1] % 2
                        best_diff[pa][pb] = max(best_diff[pa][pb], count_b[l-1] - count_a[l-1])
                        l += 1

                    pa = count_a[r] % 2
                    pb = count_b[r] % 2
                    diff = best_diff[pa ^ 1][pb]
                    if diff != -inf:
                        result = max(result, count_a[r] - count_b[r] + diff)
        
        return -1 if result == -inf else result
