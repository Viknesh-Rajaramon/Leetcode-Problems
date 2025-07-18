from imports import *

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        max_heap = [-num for num in nums[ : n]]
        heapify(max_heap)
        result = [-sum(max_heap)]
        for i in range(n, 2*n):
            curr_total = result[-1]
            if -nums[i] > max_heap[0]:
                curr_total -= -heappushpop(max_heap, -nums[i])
                curr_total += nums[i]

            result.append(curr_total)
        
        min_heap = nums[2*n : ]
        heapify(min_heap)
        curr_total = sum(min_heap)
        result[n] -= curr_total
        for i in range(2*n-1, n-1, -1):
            if nums[i] > min_heap[0]:
                curr_total -= heappushpop(min_heap, nums[i])
                curr_total += nums[i]

            result[i - n] -= curr_total
        
        return min(result)
