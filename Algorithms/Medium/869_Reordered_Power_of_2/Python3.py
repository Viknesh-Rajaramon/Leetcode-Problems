from math import log2

nums = []
for i in range(int(log2(10**9)) + 1):
    nums.append(sorted(str(2**i)))

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return sorted(str(n)) in nums
