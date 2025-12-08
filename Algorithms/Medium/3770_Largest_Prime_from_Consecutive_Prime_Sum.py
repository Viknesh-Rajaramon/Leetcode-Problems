from imports import *

MAX = 5 * 10**5
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(sqrt(MAX))+1):
    if is_prime[i]:
        for m in range(i*i, MAX+1, i):
            is_prime[m] = False

sum_primes, curr = [], 0            
for i in range(MAX):
    if is_prime[i]:
        curr += i
        if curr <= MAX and is_prime[curr]:
            sum_primes.append(curr)

class Solution:
    def largestPrime(self, n: int) -> int:
        idx = bisect_right(sum_primes, n)
        if idx == 0:
            return 0
        
        return sum_primes[idx-1]
