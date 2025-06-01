from imports import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        self.curr_capacity = 0
        
        n = len(nums)
        i = 0
        while i < min(k, n):
            heappush(self.min_heap, nums[i])
            self.curr_capacity += 1
            i += 1
        
        while i < n:
            if nums[i] > self.min_heap[0]:
                heappushpop(self.min_heap, nums[i])
            
            i += 1

    def add(self, val: int) -> int:
        if self.curr_capacity < self.k:
            heappush(self.min_heap, val)
            self.curr_capacity += 1

        elif val > self.min_heap[0]:
            heappushpop(self.min_heap, val)
        
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
