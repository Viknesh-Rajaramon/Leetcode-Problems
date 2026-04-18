from collections import Counter

class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        result, freq = [], Counter(s)
        for c in s:
            while result and freq[result[-1]] > 1 and c < result[-1]:
                freq[result.pop()] -= 1
            
            result.append(c)
        
        while freq[result[-1]] > 1:
            freq[result.pop()] -= 1

        return "".join(result)
