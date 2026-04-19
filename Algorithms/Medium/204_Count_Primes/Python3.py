max_num = 5 * 10**6

primes = []
sieve = [True for i in range(max_num+1)]
sieve[0] = False
sieve[1] = False

for i in range(2, max_num+1):
    if not sieve[i]:
        continue
    
    primes.append(i)
    for j in range(i, max_num+1, i):
        sieve[j] = False

class Solution:
    def countPrimes(self, n: int) -> int:
        low, high = 0, len(primes) - 1
        while low <= high:
            mid = (low + high) // 2
            
            if primes[mid] == n:
                return mid
            elif primes[mid] < n:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
