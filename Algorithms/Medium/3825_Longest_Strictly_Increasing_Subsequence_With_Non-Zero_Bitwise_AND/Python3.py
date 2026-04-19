from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            dp, mask = [], (1 << i)
            for num in nums:
                if num & mask == 0:
                    continue
                
                low, high = 0, len(dp)
                while low < high:
                    mid = (low + high) // 2
                    if dp[mid] < num:
                        low = mid + 1
                    else:
                        high = mid
                
                if low < len(dp) and dp[low] == num:
                    continue
                
                if low == len(dp):
                    dp.append(num)
                else:
                    dp[low] = num
            
            if result < len(dp):
                result = len(dp)

        return result
