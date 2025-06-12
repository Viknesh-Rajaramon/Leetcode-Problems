from imports import *

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def check_indices(nums: List[int], s: set) -> int:
            answer = 0
            for num in nums:
                if num in s:
                    answer += 1

            return answer
        
        return [check_indices(nums1, set(nums2)), check_indices(nums2, set(nums1))]
