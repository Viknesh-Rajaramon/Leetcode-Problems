from math import inf
from collections import deque

class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        def best_single():
            queue, best = deque(), -inf
            for i in range(1, n+1):
                j = i-l
                if j >= 0:
                    while queue and queue[-1][1] >= prefix[j]:
                        queue.pop()
                    
                    queue.append((j, prefix[j]))

                while queue and queue[0][0] < i-r:
                    queue.popleft()

                if queue:
                    best = max(best, prefix[i] - queue[0][1])

            return best

        single = best_single()
        def check(cost):
            dp_val, dp_cnt, queue = [0] * (n+1), [0] * (n+1), deque()
            for i in range(1, n+1):
                j = i-l
                if j >= 0:
                    val, cnt = dp_val[j] - prefix[j], dp_cnt[j]
                    while queue and (queue[-1][1] < val or (queue[-1][1] == val and queue[-1][2] >= cnt)):
                        queue.pop()

                    queue.append((j, val, cnt))

                while queue and queue[0][0] < i-r:
                    queue.popleft()

                dp_val[i], dp_cnt[i] = dp_val[i-1], dp_cnt[i-1]
                if queue:
                    val, cnt = prefix[i] - cost + queue[0][1], queue[0][2] + 1
                    if val > dp_val[i] or (val == dp_val[i] and cnt < dp_cnt[i]):
                        dp_val[i], dp_cnt[i] = val, cnt

            return dp_val[n], dp_cnt[n]

        val, cnt = check(0)
        if cnt <= m:
            return val if cnt > 0 else single

        low, high = 0, sum(abs(x) for x in nums) + 1
        while low < high:
            mid = (low+high) >> 1
            val, cnt = check(mid)
            if cnt > m:
                low = mid+1
            else:
                high = mid

        val, cnt = check(low)
        return max(single, val + low*m)
