from math import gcd

class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def score(arr: list[int]) -> int:
            m = len(arr)
            if m == 1:
                return 0
            
            suffix = [0] * (m-1) + [arr[m-1]]
            for i in range(m-2, -1, -1):
                suffix[i] = gcd(suffix[i+1], arr[i])
            
            ans, left_gcd = 0, 0
            for i in range(m-1):
                left_gcd = gcd(left_gcd, arr[i])
                if left_gcd == suffix[i+1]:
                    ans += 1

            return ans
        
        result, n = score(nums), len(nums)
        if n <= 2:
            return result

        g = 0
        for i in range(n):
            if i > 0 and gcd(g, nums[i]) != g:
                result = max(result, score(nums[ : i] + nums[i+1 : ]))
            
            g = gcd(g, nums[i])
        
        g = 0
        for i in range(n-1, -1, -1):
            if i < n-1 and gcd(g, nums[i]) != g:
                result = max(result, score(nums[ : i] + nums[i+1 : ]))
            
            g = gcd(g, nums[i])
        
        return result
