from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def hamming_distance(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
                    if count > 1:
                        return False
            
            return count == 1
        
        n = len(words)
        dp = [1] * n
        prev = [-1] * n
        max_index = 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamming_distance(words[i], words[j]) and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > dp[max_index]:
                max_index = i

        result = []
        i = max_index
        while i >= 0:
            result.append(words[i])
            i = prev[i]
        
        result.reverse()
        return result
