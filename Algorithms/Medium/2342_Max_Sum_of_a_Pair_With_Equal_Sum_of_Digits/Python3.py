from typing import List
from collections import defaultdict

class Solution:
    def sum_digits(self, num):
        sum_ = 0
        while num > 0:
            sum_ += num % 10
            num //= 10
        
        return sum_

    def maximumSum(self, nums: List[int]) -> int:
        sum_digits_map = defaultdict(int)
        max_num_map = defaultdict(int)
        count_map = defaultdict(int)

        for i in range(len(nums)):
            sum_of_digits = self.sum_digits(nums[i])
            count_map[sum_of_digits] += 1

            if max_num_map[sum_of_digits] + nums[i] > sum_digits_map[sum_of_digits]:
                sum_digits_map[sum_of_digits] = max_num_map[sum_of_digits] + nums[i]
            
            if max_num_map[sum_of_digits] < nums[i]:
                max_num_map[sum_of_digits] = nums[i]
        
        max_sum = -1
        
        for key, value in count_map.items():
            if value > 1 and max_sum < sum_digits_map[key]:
                max_sum = sum_digits_map[key]
        
        return max_sum
