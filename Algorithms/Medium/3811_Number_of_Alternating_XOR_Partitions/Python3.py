from typing import List

class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod, prefix_xor, dp1, dp2, result1, result2 = 10**9+7, 0, {0: 1}, {}, 0, 0
        for num in nums:
            prefix_xor ^= num
            n1, n2 = dp1.get(prefix_xor ^ target1, 0), dp2.get(prefix_xor ^ target2, 0)
            new_dp1, new_dp2 = {}, {}

            if n1:
                new_dp2[prefix_xor] = n1 % mod
            
            if n2:
                new_dp1[prefix_xor] = n2 % mod
            
            for key, val in dp1.items():
                new_dp1[key] = (new_dp1.get(key, 0) + val) % mod
            
            for key, val in dp2.items():
                new_dp2[key] = (new_dp2.get(key, 0) + val) % mod

            dp1, dp2, result1, result2 = new_dp1, new_dp2, n1, n2

        return (result1 + result2) % mod
