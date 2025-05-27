from imports import *

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        spf = list(range(max_num + 1))
        for i in range(2, int(sqrt(max_num))+1):
            if spf[i] == i:
                for j in range(i*i, max_num+1, i):
                    if spf[j] == j:
                        spf[j] = i
        
        def distinct_prime_factors(num: int) -> int:
            if num == 1:
                return 0
            
            s = set()
            while num > 1:
                s.add(spf[num])
                num = num // spf[num]
            
            return len(s)
        
        n = len(nums)
        mod = 10**9 + 7
        prime_scores = [distinct_prime_factors(nums[i]) for i in range(n)]
        left = [-1] * n
        right = [n] * n
        
        stack = deque()
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)
        
        stack = deque()
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]
            
            stack.append(i)
        
        ranges = [(i - left[i]) * (right[i] - i) for i in range(n)]

        heap = []
        for i in range(n):
            heappush(heap, (-nums[i], ranges[i]))
        
        ans = 1
        while k > 0:
            num, count = heappop(heap)
            use = min(count, k)
            ans = (ans * pow(-num, use, mod)) % mod
            k -= use
        
        return ans
