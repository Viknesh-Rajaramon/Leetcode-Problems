from typing import List
from math import inf
from heapq import heappush, heappop, heapify
from itertools import pairwise

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(inf)
        prev, nxt = list(range(-1, n)), list(range(1, n+1))
        
        min_heap = [(a+b, i) for i, (a, b) in enumerate(pairwise(nums))]
        heapify(min_heap)
        
        result, bad = 0, n - sum(1 for a, b in pairwise(nums) if a <= b)
        while bad:
            sum_, i = heappop(min_heap)
            r = nxt[i]
            if prev[r] != i or nums[i] + nums[r] != sum_:
                continue
            
            rr = nxt[r]
            bad += (nums[prev[i]] <= nums[i]) + (nums[i] <= nums[r]) + (nums[r] <= nums[rr])
            
            prev[rr], nxt[i] = i, rr
            nums[i] = sum_
            
            bad -= 1 + (nums[prev[i]] <= nums[i]) + (nums[i] <= nums[rr])

            if i:
                heappush(min_heap, (nums[prev[i]] + nums[i], prev[i]))
            if rr < n:
                heappush(min_heap, (nums[i] + nums[rr], i))

            result += 1

        return result
