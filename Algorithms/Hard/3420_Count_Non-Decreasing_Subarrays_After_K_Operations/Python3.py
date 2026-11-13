from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        result, n, nums, stack, l, ops = 0, len(nums), nums[ : : -1], [], 0, 0
        for r in range(n):
            while stack and nums[stack[-1]] < nums[r]:
                j = stack.pop()
                i = stack[-1] if stack else l-1
                ops += (nums[r] - nums[j]) * (j - i)

            stack.append(r)
            while ops > k:
                ops -= max(0, nums[stack[0]] - nums[l])
                if stack[0] == l:
                    stack.pop(0)
                
                l += 1

            result += r-l+1

        return result
