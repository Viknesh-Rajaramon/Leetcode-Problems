from imports import *

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        def count_zero(nums: List[int]) -> int:
            zero_count = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_count += 1
            
            return zero_count

        counter1 = Counter(nums1)
        sum1 = sum(nums1) + counter1[0]

        counter2 = Counter(nums2)
        sum2 = sum(nums2) + counter2[0]

        if sum1 == sum2:
            return sum1
        elif sum1 < sum2:
            if counter1[0] != 0:
                return sum2
            else:
                return -1
        else:
            if counter2[0] != 0:
                return sum1
            else:
                return -1
        
        return -1
