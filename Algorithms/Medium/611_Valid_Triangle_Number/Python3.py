from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n, result = len(nums), 0
        for i in range(n-1, 1, -1):
            if nums[0] + nums[1] > nums[i]:
                result += (i+1) * i * (i-1) // 6
                break
            
            if nums[i-2] + nums[i-1] < nums[i]:
                continue
            
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1

        return result
