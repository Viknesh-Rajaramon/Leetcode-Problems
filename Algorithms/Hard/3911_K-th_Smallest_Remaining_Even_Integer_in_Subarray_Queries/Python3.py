from bisect import bisect_left, bisect_right

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
        prefix = [(nums[arr[0]]-2) // 2] if arr else []
        for i in range(len(arr)-1):
            prefix.append((nums[arr[i+1]] - nums[arr[i]] - 2) // 2)
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
        
        result = []
        for l, r, k in queries:
            left, right = bisect_left(arr, l), bisect_right(arr, r)-1
            if left >= len(arr) or right < 0:
                result.append(2*k)
                continue
            
            first, last = nums[arr[left]] // 2, nums[arr[right]] // 2
            if k < first:
                result.append(2*k)
            elif last-right+left <= k:
                k += right - left + 1
                result.append(2*k)
            else:
                k -= left
                idx = bisect_left(prefix, k) - 1
                result.append(nums[arr[idx]] + 2*(k - prefix[idx]))

        return result
