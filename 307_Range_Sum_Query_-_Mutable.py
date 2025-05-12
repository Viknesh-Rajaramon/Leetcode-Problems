from imports import *

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum_ = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.sum_ -= self.nums[index] - val
        self.nums[index]  = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_ - sum(self.nums[ : left]) - sum(self.nums[right+1: ])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
