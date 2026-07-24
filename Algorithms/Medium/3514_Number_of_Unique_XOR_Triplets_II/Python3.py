from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs, triplets, k = {0}, set(nums), 1 << max(nums).bit_length()
        while nums:
            num = nums.pop()
            triplets |= {num ^ x for x in pairs}
            pairs |= {num ^ x for x in nums}

            if len(triplets) == k:
                return k

        return len(triplets)
