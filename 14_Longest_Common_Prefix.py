from imports import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        min_length = inf
        for i in range(n):
            min_length = min(min_length, len(strs[i]))

        prefix = ""
        for i in range(min_length):
            for j in range(1, n):
                if strs[j][i] != strs[0][i]:
                    return prefix
            
            prefix = prefix + strs[0][i]
        
        return prefix
