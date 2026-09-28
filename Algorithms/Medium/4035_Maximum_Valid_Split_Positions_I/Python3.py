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

        result = score(nums)
        for i in range(len(nums)):
            result = max(result, score(nums[ : i] + nums[i+1 : ]))
        
        return result
