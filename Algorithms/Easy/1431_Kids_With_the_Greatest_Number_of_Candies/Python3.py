from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        ans = []
        for c in candies:
            if c + extraCandies < maxCandies:
                ans.append(False)
            else:
                ans.append(True)
        
        return ans
