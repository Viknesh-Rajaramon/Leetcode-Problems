from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        large, small, freq = SortedList(), SortedList(), defaultdict(int)
        def insert(num: int) -> int:
            ans, p = 0, (freq[num], num)
            if len(large) < x or p > large[0]:
                ans += p[0] * p[1]
                large.add(p)
                if len(large) > x:
                    to_remove = large[0]
                    ans -= to_remove[0] * to_remove[1]
                    large.remove(to_remove)
                    small.add(to_remove)
            else:
                small.add(p)
            
            return ans
        
        def remove(num: int):
            ans, p = 0, (freq[num], num)
            if p >= large[0]:
                ans -= p[0] * p[1]
                large.remove(p)
                if small:
                    to_add = small[-1]
                    ans += to_add[0] * to_add[1]
                    small.remove(to_add)
                    large.add(to_add)
            else:
                small.remove(p)
            
            return ans

        result, ans = [], 0
        for i, num in enumerate(nums):
            if freq[num] > 0:
                ans += remove(num)

            freq[num] += 1
            ans += insert(num)
            
            if i >= k:
                ans += remove(nums[i-k])
                freq[nums[i-k]] -= 1
                if freq[nums[i-k]] > 0:
                    ans += insert(nums[i-k])
            
            if i >= k-1:
                result.append(ans)
        
        return result
