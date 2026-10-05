from bisect import bisect_left

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        first, last, pos, prefix = [n+1] * k, [-1] * k, [[] for _ in range(k)], 0
        first[0], last[0] = 0, 0
        for i in range(n):
            val = ((nums[i] % k) + k) % k
            pos[val].append(i)
            prefix = (prefix + val) % k
            last[prefix] = i+1
            if first[prefix] == n+1:
                first[prefix] = i+1
        
        result = 0
        for i in range(k):
            if first[i] != n+1:
                result = max(result, last[i] - first[i])
        
        for i in range(k):
            if not pos[i]:
                continue
            
            target = (2*i) % k
            for j in range(k):
                if first[j] == n+1:
                    continue
                
                r = (j+target)%k
                if last[r] == -1 or last[r] - first[j] <= result:
                    continue
                
                idx = bisect_left(pos[i], first[j])
                if idx < len(pos[i]) and pos[i][idx] < last[r]:
                    result = last[r] - first[j]

        return result
