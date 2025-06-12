class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i, c in enumerate(s):
            result += abs(i - t.find(c))
        
        return result
