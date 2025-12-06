from imports import *

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        left, count, mod, dp, min_queue, max_queue = 0, 1, 10**9+7, [1], deque(), deque()
        for num in nums:
            while min_queue and num < min_queue[-1]:
                min_queue.pop()
            
            while max_queue and num > max_queue[-1]:
                max_queue.pop()
            
            min_queue.append(num)
            max_queue.append(num)

            while max_queue[0] - min_queue[0] > k:
                count -= dp[left]
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                
                left += 1
            
            dp.append(count)
            count = (count * 2) % mod
        
        return dp[-1] % mod
