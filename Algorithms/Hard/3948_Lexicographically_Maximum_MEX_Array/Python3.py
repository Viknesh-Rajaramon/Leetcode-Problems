from typing import List

class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n, mx, mex, curr_mex = len(nums), 10**5+2, 0, 0
        total_cnt, curr_cnt = [0] * mx, [0] * mx
        for num in nums:
            total_cnt[num] += 1
        
        while total_cnt[mex]:
            mex += 1
        
        result, l = [], 0
        for r in range(n):
            curr_cnt[nums[r]] += 1
            while curr_cnt[curr_mex]:
                curr_mex += 1
            
            if curr_mex == mex:
                result.append(mex)
                for i in range(l, r+1):
                    total_cnt[nums[i]] -= 1
                    curr_cnt[nums[i]] -= 1
                    if total_cnt[nums[i]] == 0:
                        mex = min(mex, nums[i])

                curr_mex, l = 0, r+1
        
        return result
