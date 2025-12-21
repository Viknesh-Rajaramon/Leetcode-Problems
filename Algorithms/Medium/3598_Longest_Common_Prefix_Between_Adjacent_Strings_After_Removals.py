from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def lcp_length(word1: str, word2: str) -> int:
            n = min(len(word1), len(word2))
            for i in range(n):
                if word1[i] != word2[i]:
                    return i

            return n

        n = len(words)
        if n <= 2:
            return [0] * n
        
        prefix = [0] * n
        suffix = [0] * n

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], lcp_length(words[i-1], words[i]))

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], lcp_length(words[i], words[i+1]))

        result = [suffix[1]]
        for i in range(1, n-1):
            result.append(max(prefix[i-1], suffix[i+1], lcp_length(words[i-1], words[i+1])))

        return result + [prefix[n-2]]
