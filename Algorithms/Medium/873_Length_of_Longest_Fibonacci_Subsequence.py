from imports import *

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        dp = [[0] * n for _ in range(n)]

        arr_map = {num: idx for idx, num in enumerate(arr)}

        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                idx = arr_map.get(arr[i]+arr[j], -1)
                length = 2

                if idx != -1:
                    length = 1 + dp[j][idx]
                    max_len = max(max_len, length)

                dp[i][j] = length
        
        return max_len
