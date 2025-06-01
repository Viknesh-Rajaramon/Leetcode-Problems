from imports import *

class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = [i+1 for i in range(1000)]
        self.nums = defaultdict(lambda: True)

    def popSmallest(self) -> int:
        num = heappop(self.min_heap)
        self.nums[num] = False
        return num

    def addBack(self, num: int) -> None:
        if not self.nums[num]:
            heappush(self.min_heap, num)
            self.nums[num] = True

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
