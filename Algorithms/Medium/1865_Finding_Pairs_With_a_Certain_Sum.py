from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)
        self.keys = sorted(self.freq1.keys())

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for num in self.keys:
            if num >= tot:
                break
            
            if tot - num in self.freq2:
                result += self.freq2[tot - num] * self.freq1[num]

        return result


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
