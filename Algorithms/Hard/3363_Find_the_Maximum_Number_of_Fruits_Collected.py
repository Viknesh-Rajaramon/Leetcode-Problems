from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        result = sum(fruits[i][i] for i in range(n))
        right, bottom = [fruits[0][n-1], 0, 0], [fruits[n-1][0], 0, 0]
        max_reachable = 2
        for i in range(1, n-1):
            right_n, bottom_n = [0] * (max_reachable+2), [0] * (max_reachable+2)

            for j in range(max_reachable):
                right_n[j] = max(right[j-1], right[j], right[j+1]) + fruits[i][n-1-j]
                bottom_n[j] = max(bottom[j-1], bottom[j], bottom[j+1]) + fruits[n-1-j][i]
            
            right, bottom = right_n, bottom_n
            
            if max_reachable > n-i-2:
                max_reachable -= 1
            else:
                max_reachable += 1
                
        return result + right[0] + bottom[0]
