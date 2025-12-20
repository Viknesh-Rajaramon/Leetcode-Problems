from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for cust in accounts:
            total = sum(cust)
            if max_wealth < total:
                max_wealth = total
        
        return max_wealth
