from math import sqrt

MAX_ = 10**5+5
primes = [True] * (MAX_+1)
primes[0], primes[1] = False, False
for i in range(2, int(sqrt(MAX_))+1):
    if primes[i]:
        for j in range(i*i, MAX_, i):
            primes[j] = False

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            j = nums[i]
            if i & 1:
                while primes[j]:
                    result += 1
                    j += 1
            else:
                while not primes[j]:
                    result += 1
                    j += 1
        
        return result
