class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        currfreq1 = {}
        currfreq3 = {}
        i1 = 0
        i3 = 0
        distinct1 = 0

        enough = 0 
        res = 0
        for j, a in enumerate(nums):
            if a not in currfreq1:
                currfreq1[a] = 0
                distinct1 += 1
            if a not in currfreq3:
                currfreq3[a] = 0
            currfreq1[a] += 1
            currfreq3[a] += 1
            if currfreq3[a] == m:
                enough += 1 

            while distinct1 > k:
                currfreq1[nums[i1]] -= 1
                if currfreq1[nums[i1]] == 0:
                    del currfreq1[nums[i1]]
                    distinct1 -= 1
                i1 += 1

            while enough >= k:
                if currfreq3[nums[i3]] == m:
                    enough -= 1
                currfreq3[nums[i3]] -= 1
                if currfreq3[nums[i3]] == 0:
                    del currfreq3[nums[i3]]
                i3 += 1
            
            if i3 > i1:
                res += i3 - i1

        return res
