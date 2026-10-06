from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result, freq = [], Counter(nums)
        keys, max_freq = sorted(freq.keys()), max(freq.values())
        for i in range(1, max_freq+1):
            for key in keys:
                if freq[key] >= i:
                    result.append(key)
        
        return result
