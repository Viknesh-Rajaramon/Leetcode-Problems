class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        prev_one, next_one, left, right = [-1] * 31, [n] * 31, [0] * n, [n-1] * n
        for i in range(n):
            for bit in range(31):
                if nums[i] & (1 << bit) == 0:
                    left[i] = max(left[i], prev_one[bit]+1)
                else:
                    prev_one[bit] = i

        for i in range(n-1, -1, -1):
            for bit in range(31):
                if nums[i] & (1 << bit) == 0:
                    right[i] = min(right[i], next_one[bit]-1)
                else:
                    next_one[bit] = i

        result, last_idx = 0, {}
        for i in range(n):
            l, r = left[i], right[i]
            if nums[i] in last_idx:
                l = max(l, last_idx[nums[i]] + 1)
            
            last_idx[nums[i]] = i
            result += (i-l+1) * (r-i+1)

        return result
