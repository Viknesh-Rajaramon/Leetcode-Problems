from collections import Counter

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        values = sorted(freq.keys())
        n = len(values)
        for i in range(n):
            for j in range(i+1, n):
                if freq[values[i]] != freq[values[j]]:
                    return [values[i], values[j]]
        
        return [-1, -1]
