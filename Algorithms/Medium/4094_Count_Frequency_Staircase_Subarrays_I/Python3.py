from collections import defaultdict

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ind, pos = [0] * n, defaultdict(list)
        for i, a in enumerate(nums):
            ind[i] = len(pos[a])
            pos[a].append(i)

        result = 0
        for i in range(n):
            seen, l, r = set(), i, n-1
            for j in range(i, n):
                if j > r:
                    break
                
                if nums[j] in seen:
                    continue
                
                seen.add(nums[j])
                k = len(seen)
                if ind[j]+k-1 >= len(pos[nums[j]]):
                    break
                
                l = max(l, pos[nums[j]][ind[j] + k - 1])
                r = min(r, pos[nums[j]][ind[j] + k] if ind[j] + k < len(pos[nums[j]]) else n-1)
                if l > r:
                    break
                
                if l <= i + k*(k + 1) // 2 - 1 <= r:
                    result += 1
        
        return result
