from collections import deque

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod, dp_0, dp_1 = 10**9+7, [0] * (one+1), [0] * (one+1)
        for j in range(1, min(one, limit)+1):
            dp_1[j] = 1

        dp_1_queue = deque([dp_1[ : ]])
        for i in range(1, zero+1):
            new_dp_0, new_dp_1 = [0] * (one+1), [0] * (one+1)
            if i <= limit:
                new_dp_0[0] = 1

            for j in range(one):
                new_dp_0[j+1] = (dp_0[j+1] + dp_1[j+1] - (dp_1_queue[0][j+1] if i > limit else 0)) % mod
                new_dp_1[j+1] = (new_dp_0[j] + new_dp_1[j] - (new_dp_0[j-limit] if j >= limit else 0)) % mod

            dp_1_queue.append(new_dp_1[ : ])
            if len(dp_1_queue) > limit+1:
                dp_1_queue.popleft()

            dp_0, dp_1 = new_dp_0, new_dp_1

        return (dp_0[one] + dp_1[one]) % mod
