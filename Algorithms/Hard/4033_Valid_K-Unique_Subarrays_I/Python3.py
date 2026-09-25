from math import sqrt

class Mo:
    def __init__(self, k: int):
        self.freq = {}
        self.odd_freq = set()
        self.k = k
            
    def add(self, num: int) -> None:
        if num in self.freq:
            self.freq[num] += 1
        else:
            self.freq[num] = 1

        if num in self.odd_freq:
            self.odd_freq.remove(num)
        else:
            self.odd_freq.add(num)

    def remove(self, num: int) -> None:
        self.freq[num] -= 1
        if self.freq[num] == 0:
            del self.freq[num]

        if num in self.odd_freq:
            self.odd_freq.remove(num)
        else:
            self.odd_freq.add(num)
            
    def check(self) -> bool:
        return len(self.freq) == self.k and len(self.odd_freq) == 0

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        q, blockSize = len(queries), max(1, int(sqrt(len(nums))))
        queries = [(l, r, i) for i, (l, r) in enumerate(queries)]
        queries.sort(key = lambda x: (x[0] // blockSize, x[1] if (x[0] // blockSize)%2==0 else -x[1]))
        result, l, r = [False] * q, 0, -1
        mo = Mo(k)
        for start, end, i in queries:
            while l > start:
                l -= 1
                mo.add(nums[l])
            
            while r < end:
                r += 1
                mo.add(nums[r])

            while l < start:
                mo.remove(nums[l])
                l += 1
            
            while r > end:
                mo.remove(nums[r])
                r -= 1

            result[i] = mo.check()

        return result
