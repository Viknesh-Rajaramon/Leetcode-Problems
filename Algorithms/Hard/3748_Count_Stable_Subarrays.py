from imports import *

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        R = [0] * (n-1) + [n-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] if nums[i] <= nums[i+1] else i

        L = [0] * n
        for i in range(1, n):
            L[i] = L[i-1] if nums[i-1] <= nums[i] else i

        segments, i = [], 0
        while i < n:
            segments.append((i, R[i]))
            i = R[i] + 1

        prefix_sum = [0]
        for start, end in segments:
            length = end - start + 1
            prefix_sum.append(prefix_sum[-1] + length * (length+1))

        result, starts = [], [s for s, _ in segments]
        for l, r in queries:
            seg_l, seg_r = bisect_right(starts, l) - 1, bisect_right(starts, r) - 1
            if seg_l == seg_r:
                length = r - l + 1
                result.append(length * (length+1) // 2)
                continue

            len_left, len_right = R[l] - l + 1, r - L[r] + 1
            ans = len_left * (len_left + 1) + len_right * (len_right + 1)
            
            if seg_l + 2 <= seg_r:
                ans += prefix_sum[seg_r] - prefix_sum[seg_l + 1]

            result.append(ans // 2)

        return result
