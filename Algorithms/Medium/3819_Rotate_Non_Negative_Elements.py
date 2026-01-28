from typing import List

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        arr = [i for i, num in enumerate(nums) if num >= 0]
        n = len(arr)
        if n == 0:
            return nums
        
        k %= n
        if k == 0:
            return nums
        
        result = nums[:]
        for i in range(n):
            result[arr[i % n]] = nums[arr[(i+k) % n]]

        return result
