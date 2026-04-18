from math import inf

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        def solve(k: int) -> bool:
            chunks, min_max = n//k, []
            for i in range(chunks):
                start, min_, max_, count = i*k, inf, -inf, 0
                for j in range(k):
                    curr, nxt = nums[start+j], nums[start+(j+1)%k]
                    min_, max_ = min(min_, curr), max(max_, curr)
                    if curr > nxt:
                        count += 1
                    
                if count > 1:
                    return False

                min_max.append((min_, max_))
            
            for i in range(chunks-1):
                if min_max[i][1] > min_max[i+1][0]:
                    return False
            
            return True

        result, i = 0, 1
        while i*i <= n:
            if n%i == 0:
                if solve(i):
                    result += i
                
                temp = n//i
                if i != temp and solve(temp):
                    result += temp

            i += 1

        return result
