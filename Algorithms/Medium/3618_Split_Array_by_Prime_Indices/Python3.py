from typing import List

MAX_N = 10**5
PRIMES = []

sieve = [True] * (MAX_N - 1)
for i in range(2, MAX_N+1):
    if not sieve[i-2]:
        continue

    PRIMES.append(i)
    for j in range(2*i, MAX_N+1, i):
        sieve[j-2] = False

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        sum_a, sum_b = 0, 0
        idx = 0
        for i in range(len(nums)):
            if idx < len(PRIMES) and i == PRIMES[idx]:
                sum_a += nums[i]
                idx += 1
            else:
                sum_b += nums[i]

        return abs(sum_a - sum_b)
