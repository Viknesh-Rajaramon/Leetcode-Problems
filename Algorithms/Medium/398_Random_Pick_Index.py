from imports import *

class Solution:

    def __init__(self, nums: List[int]):
        self.hash_map = defaultdict(list)
        for i in range(len(nums)):
            self.hash_map[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.hash_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
