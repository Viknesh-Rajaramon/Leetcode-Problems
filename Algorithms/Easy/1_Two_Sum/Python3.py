from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {v: i for i, v in enumerate(nums)}
        
        for i in range(len(nums)):
            num_j = target - nums[i]
            if num_j in index_map and i != index_map[num_j]:
                return [i, index_map[num_j]]
        
        return [0, 0]
