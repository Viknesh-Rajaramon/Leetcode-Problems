from imports import *

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        if sum(freq[c] % 2 for c in freq) > 1:
            return ""
        
        n, sorted_chars, odd = len(s), "".join(sorted(freq.keys())), ""
        if n % 2:
            for c in sorted_chars:
                if freq[c] % 2:
                    odd = c
                    break
        
        for c in freq.keys():
            freq[c] = freq[c] // 2
        
        result, path = "", ""
        def dfs(i: int, tight: bool) -> None:
            nonlocal result, path
            if result:
                return
            
            if i == n // 2:
                if not tight or path + odd + path[::-1] > target:
                    result = path + odd + path[::-1]
                
                return
            
            low = "" if not tight else target[i]
            for c in sorted_chars:
                if c >= low and freq[c]:
                    path += c
                    freq[c] -= 1
                    dfs(i+1, tight and c == low)
                    path = path[:-1]
                    freq[c] += 1
                    if result:
                        break
        
        dfs(0, True)
        return result
