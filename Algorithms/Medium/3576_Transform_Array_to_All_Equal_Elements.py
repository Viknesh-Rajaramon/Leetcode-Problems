from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def ops_to_make_equal(target: int) -> bool:
            arr = nums[:]
            ops = 0
            for i in range(n-1):
                if arr[i] != target:
                    arr[i] = target
                    arr[i+1] *= -1
                    ops += 1
                    if ops > k:
                        return False

            return all(num == target for num in arr)

        return ops_to_make_equal(1) or ops_to_make_equal(-1)
