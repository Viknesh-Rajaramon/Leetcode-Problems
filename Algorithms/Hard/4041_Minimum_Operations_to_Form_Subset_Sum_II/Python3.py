from math import inf

class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = [inf] * (sum+1)
        dp[0] = 0
        for num in nums:
            costs, value, divisions = {}, num, 0
            while value:
                current, multiplications = value, 0
                while current <= sum:
                    cost = divisions + multiplications
                    if cost < costs.get(current, inf):
                        costs[current] = cost
                    
                    if current > (sum >> 1):
                        break
                    
                    current <<= 1
                    multiplications += 1

                value >>= 1
                divisions += 1

            next_dp = dp[ : ]
            for value, cost in costs.items():
                for current_sum in range(sum-value+1):
                    if dp[current_sum] != inf:
                        candidate = dp[current_sum] + cost
                        if candidate < next_dp[current_sum + value]:
                            next_dp[current_sum + value] = candidate

            dp = next_dp

        return -1 if dp[sum] == inf else dp[sum]
