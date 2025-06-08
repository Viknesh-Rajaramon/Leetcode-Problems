from imports import *

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        indexes = defaultdict(list)

        n = len(nums)
        for i in range(n):
            counts[nums[i]] += 1
            indexes[nums[i]].append(i)
        
        max_count, max_count_num, min_length = 0, -1, 0
        for num, count in counts.items():
            if max_count < count:
                max_count = count
                max_count_num = num
                min_length = indexes[num][-1] - indexes[num][0]
            elif max_count == count and indexes[num][-1] - indexes[num][0] < min_length:
                max_count_num = num
                min_length = indexes[num][-1] - indexes[num][0]
        
        return min_length + 1
