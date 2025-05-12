from imports import *

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        vowels = set(["a", "e", "i", "o", "u"])

        i = 0
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix_sum.append(prefix_sum[i] + 1)
            else:
                prefix_sum.append(prefix_sum[i])
            
            i += 1

        result = []
        for l, r in queries:
            result.append(prefix_sum[r+1] - prefix_sum[l])
            
        return result
