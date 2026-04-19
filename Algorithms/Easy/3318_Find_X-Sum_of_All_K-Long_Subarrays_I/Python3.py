from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result, n, freq = [], len(nums), {}
        for i in range(k):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        for i in range(n-k+1):
            top = sorted(freq.items(), key = lambda p: (p[1], p[0]), reverse = True)
            result.append(sum(val * f for val, f in top[:x]))

            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]
            
            if i + k < n:
                if nums[i+k] not in freq:
                    freq[nums[i+k]] = 1
                else:
                    freq[nums[i+k]] += 1

        return result
