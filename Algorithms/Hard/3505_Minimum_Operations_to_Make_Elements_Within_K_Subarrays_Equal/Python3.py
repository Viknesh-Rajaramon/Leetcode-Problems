from typing import List
from math import inf
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n, l_size, r_size = len(nums), x//2, x - x//2
        init = sorted([(num, i) for i, num in enumerate(nums[ : x])])
        mid, left, right, cost = init[l_size][0], [], [], 0
        for j in range(x):
            num, i = init[j]
            cost += abs(num - mid)
            if j < l_size:
                heappush(left, (-num, -i))
            else:
                heappush(right, (num, i))

        costs = [inf] * x + [cost]
        for i in range(x, n):
            cost += abs(nums[i] - mid) - abs(nums[i-x] - mid)
            if nums[i-x] < right[0][0] or (nums[i-x] == right[0][0] and i-x < right[0][1]):
                while left and -left[0][1] <= i-x:
                    heappop(left)

                if nums[i] < right[0][0]:
                    heappush(left, (-nums[i], -i))
                else:
                    pop_right, pop_right_i = heappop(right)
                    while right and right[0][1] <= i-x:
                        heappop(right)

                    heappush(left, (-pop_right, -pop_right_i))
                    heappush(right, (nums[i], i))

                    cost += (l_size - r_size) * abs(right[0][0] - mid)
                    mid = right[0][0]
            else:
                while right and right[0][1] <= i-x:
                    heappop(right)

                if nums[i] >= -left[0][0]:
                    heappush(right, (nums[i], i))
                    if mid < right[0][0]:
                        cost += (l_size - r_size) * abs(right[0][0] - mid)
                    else:
                        cost += (r_size - l_size - 2) * abs(right[0][0] - mid)
                    
                    mid = right[0][0]
                else:
                    pop_left, pop_left_i = heappop(left)
                    pop_left, pop_left_i = -pop_left, -pop_left_i
                    while left and -left[0][1] <= i-x:
                        heappop(left)

                    heappush(left, (-nums[i], -i))
                    heappush(right, (pop_left, pop_left_i))
                    cost += (r_size - l_size - 2) * abs(mid - pop_left)
                    mid = pop_left
            
            costs.append(cost)

        dp = [inf]
        for i in range(n):
            dp.append(min(dp[-1], costs[i+1]))

        for _ in range(1, k):
            new_dp = [inf] * x
            for i in range(x, n+1):
                new_dp.append(min(new_dp[-1], dp[i-x] + costs[i]))

            dp = new_dp
        
        return dp[-1]
