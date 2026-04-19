from typing import List
from math import inf

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right+1)
        primes = []
        ans_primes = []
        smallest_prime_factor = [None] * (right+1)

        is_prime[0] = is_prime[1] = False

        for i in range(2, right+1):
            if is_prime[i]:
                primes.append(i)
                smallest_prime_factor[i] = i
                if i >= left:
                    ans_primes.append(i)
            
            j = 0
            while (j < len(primes) and i * primes[j] <= right and primes[j] <= smallest_prime_factor[i]):
                is_prime[i * primes[j]] = False
    
                # put smallest prime factor of i*prime[j] 
                smallest_prime_factor[i * primes[j]] = primes[j]
                
                j += 1

        if len(ans_primes) < 2:
            return [-1, -1]
        
        min_i = 0
        gap = inf
        for i in range(len(ans_primes)-1):
            diff = ans_primes[i+1] - ans_primes[i]
            if diff < gap:
                gap = diff
                min_i = i
        
        return ans_primes[min_i : min_i+2]
