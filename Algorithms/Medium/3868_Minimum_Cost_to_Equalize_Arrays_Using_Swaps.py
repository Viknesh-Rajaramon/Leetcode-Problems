from collections import defaultdict

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        freq_1, freq_total = defaultdict(int), defaultdict(int)
        for num in nums1:
            freq_1[num] += 1
            freq_total[num] += 1
        
        for num in nums2:
            freq_1[num] -= 1
            freq_total[num] += 1
        
        for count in freq_total.values():
            if count%2:
                return -1
            
        return sum(abs(diff)//2 for diff in freq_1.values()) // 2
