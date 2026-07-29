class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n, count = len(s), [0] * 26
        for i in range(n//2):
            count[ord(s[i])-ord('a')] += 1
        
        total, counting, remain, i = 0, 1, 0, 0
        for i in range(25, -1, -1):
            for c in range(1, count[i]+1):
                total += 1
                counting = counting * total // c
                if counting >= k:
                    remain = count[i] - c
                    break
            
            if counting >= k:
                break
        
        if counting < k:
            return ""

        result, l = [""] * n, 0
        for j in range(i+1):
            x, c = chr(ord('a')+j), count[j]
            if j == i:
                c = remain
            
            for _ in range(c):
                count[j] -= 1
                result[l] = x
                l += 1
        
        while total:
            for j in range(i, 26):
                if count[j] == 0:
                    continue
                
                new_count = counting * count[j] // total
                if new_count < k:
                    k -= new_count
                    continue
                
                counting = new_count
                count[j] -= 1
                total -= 1
                result[l] = chr(ord('a') + j)
                l += 1
                break
        
        if n & 1:
            result[l] = s[n//2]
            l += 1
        
        for i in range(l-1-n%2, -1, -1):
            result[l] = result[i]
            l += 1

        return "".join(result)
