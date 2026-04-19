from typing import List
from collections import defaultdict, deque

MAX = 10**6 + 1
prime_factors = defaultdict(list)
prime = [True] * MAX
for i in range(2, MAX):
    if not prime[i]:
        continue

    for j in range(i, MAX, i):
        prime_factors[j].append(i)
        if i != j:
            prime[j] = False

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        queue = deque([n-1])
        visited = set([n-1])
        
        indexes = defaultdict(list)
        for i in range(n):
            if nums[i] != 1 and prime[nums[i]]:
                indexes[nums[i]].append(i)
        
        primes_taken = defaultdict(int)
        for i in range(n+5):
            if 0 in visited:
                return i
            
            for i in range(len(queue)):
                idx = queue.popleft()
                
                nxt, prev = idx + 1, idx - 1
                if nxt < n and nxt not in visited:
                    queue.append(nxt)
                    visited.add(nxt)
                
                if prev >= 0 and prev not in visited:
                    queue.append(prev)
                    visited.add(prev)
                
                for primes in prime_factors[nums[idx]]:
                    if primes_taken[primes]:
                        continue
                    
                    primes_taken[primes] = 1
                    for idxes in indexes[primes]:
                        if idxes not in visited:
                            queue.append(idxes)
                            visited.add(idxes)
                        
        return -1
    