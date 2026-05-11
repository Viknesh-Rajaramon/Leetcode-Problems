class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_val = max(nums)
        present = [False] * (max_val+1)
        for num in nums:
            present[num] = True
        
        min_val = [0] * (max_val+1)
        for i in range(1, max_val+1):
            if not present[i]:
                continue
            
            for j in range(i, max_val+1, i):
                if min_val[j] == 0:
                    min_val[j] = i
        
        return sum(min_val[num] for num in nums)
