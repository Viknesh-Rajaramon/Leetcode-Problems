from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        ordered_nums, num_to_group, current_group, group_start = sorted(nums), {}, 0, [0]
        prev = ordered_nums[0]
        for i, x in enumerate(ordered_nums):
            if x - prev > limit:
                current_group += 1
                group_start.append(i)

            num_to_group[x], prev = current_group, x
            
        result = []
        for x in nums:
            group = num_to_group[x]
            result.append(ordered_nums[group_start[group]])
            group_start[group] += 1

        return result
