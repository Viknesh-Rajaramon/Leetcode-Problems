from imports import *

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(num: int):
            if num <= 1:
                return False
            
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    return False
            
            return True
        
        n = len(s)
        primes = set()
        for i in range(n):
            num = int(s[i])
            if num == 0:
                continue
            
            if is_prime(num):
                primes.add(num)

            for j in range(i+1, n):
                num = num * 10 + int(s[j])
                if is_prime(num):
                    primes.add(num)
        
        primes = sorted(primes, reverse = True)
        
        sum_ = 0
        for i in range(len(primes)):
            if i == 3:
                break
            
            sum_ += primes[i]

        return sum_
