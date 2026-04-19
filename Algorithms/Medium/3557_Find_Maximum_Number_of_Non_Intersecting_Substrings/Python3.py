from collections import defaultdict, deque

class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        char_index = defaultdict(deque)
        
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i]

            for j in char_index[word[i]]:
                if i - j + 1 >= 4:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)
            
            char_index[word[i]].append(i)
            if len(char_index[word[i]]) > 4:
                char_index[word[i]].popleft()
    
        return dp[-1]
