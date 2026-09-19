from bisect import bisect_right

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        result, pre, x = 0, 0, [0]
        for num in nums:
            pre += (a if num%2 == 1 else -b)
            i = bisect_right(x, pre)
            x.insert(i, pre)
            result += i

        return result
