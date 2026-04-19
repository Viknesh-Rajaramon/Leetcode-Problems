from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        result, n, seen = 0, len(nums), set()
        for i in range(n):
            seen.clear()
            balance = 0
            if result > n-i:
                break
            
            for j in range(i, n):
                if nums[j] not in seen:
                    if nums[j] % 2:
                        balance -= 1
                    else:
                        balance += 1
                    
                    seen.add(nums[j])
                
                if balance == 0:
                    result = max(result, j-i+1)
        
        return result
