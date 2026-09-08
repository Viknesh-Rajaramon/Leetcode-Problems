from typing import List

class Solution:
    def getLength(self, nums: List[int]) -> int:
        result, n = 1, len(nums)
        for l in range(n):
            count, freq, min_, max_, distinct, occupied = {}, [0] * (n+1), n+1, 0, 0, 0
            for r in range(l, n):
                old = count.get(nums[r], 0)
                new = old+1
                count[nums[r]] = new
                if old == 0:
                    distinct += 1
                    min_ = 1
                else:
                    freq[old] -= 1
                    if freq[old] == 0:
                        occupied -= 1

                if freq[new] == 0:
                    occupied += 1
                
                freq[new] += 1
                max_ = max(max_, new)

                if old > 0 and old == min_ and freq[old] == 0:
                    while freq[min_] == 0:
                        min_ += 1

                if distinct == 1 or (occupied == 2 and max_ == 2*min_):
                    result = max(result, r-l+1)

        return result
