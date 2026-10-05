from math import inf
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        even, odd = [], []
        for length in range(1, len(str(max(nums)))+1):
            half = (length+1) // 2
            for x in range(10**(half-1), 10**half):
                s = str(x)
                p = int(s + s[-2 : : -1]) if length%2 else int(s + s[ : : -1])

                if p%2:
                    odd.append(p)
                else:
                    even.append(p)

        even.sort()
        odd.sort()

        result = 0
        for num in nums:
            arr, best = even if num%2 == 0 else odd, inf
            pos = bisect_left(arr, num)
            if pos < len(arr):
                best = min(best, arr[pos] - num)

            if pos > 0:
                best = min(best, num - arr[pos-1])

            result += best // 2

        return result
