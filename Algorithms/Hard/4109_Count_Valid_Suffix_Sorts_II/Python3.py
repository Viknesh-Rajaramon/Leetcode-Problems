class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
        n, m = len(nums), len(target)
        result, com = [0] * (m-n+1), nums + [0] + target
        L_com = len(com)
        z, l, r = [0] * L_com, 0, 0
        for i in range(1, L_com):
            if i <= r:
                z[i] = min(r-i+1, z[i-l])
            
            while i + z[i] < L_com and com[z[i]] == com[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
                
        pre = [0] * m
        for i in range(1, m):
            pre[i] = pre[i-1] if target[i-1] >= target[i] else i
            
        freq, bad = [0] * 100001, 0        
        for x in nums:
            if freq[x] == 1:
                bad -= 1
            
            freq[x] -= 1
            
        for i in range(n):
            if freq[target[i]] == 0:
                bad += 1
            
            freq[target[i]] += 1
            
        zs = n+1
        for k in range(m-n+1):
            if bad == 0:
                min_I = max(0, pre[k+n-1] - k)
                max_I = min(n-1, z[zs + k])
                if max_I >= min_I:
                    result[k] = max_I - min_I + 1
                    
            if k+n < m:
                if freq[target[k]] == 1:
                    bad -= 1
                
                freq[target[k]] -= 1
                if freq[target[k+n]] == 0:
                    bad += 1
                
                freq[target[k+n]] += 1
                
        return result
