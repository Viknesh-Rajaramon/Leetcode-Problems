class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        result, n = 0, len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(n):
            for j in range(i, n):
                total = prefix[j+1] - prefix[i]
                if total % 10 != x:
                    continue

                while total >= 10:
                    total //= 10
                
                if total == x:
                    result += 1

        return result
