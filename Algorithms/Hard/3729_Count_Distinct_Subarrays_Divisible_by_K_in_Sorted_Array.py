from typing import List
from collections import defaultdict

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        result, n, map_, sum_ = 0, len(nums), defaultdict(int), 0
        map_[0] = 1
        
        i = 0
        while i < n:
            j, temp = i, sum_
            while j < n and nums[j] == nums[i]:
                temp = (temp + nums[j]) % k
                result += map_[temp]
                j += 1
            
            j = i
            while j < n and nums[j] == nums[i]:
                sum_ = (sum_ + nums[j]) % k
                map_[sum_] += 1
                j += 1
            
            i = j

        return result
