from typing import List

class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        n = len(demand)
        def check(wait_limit: int) -> int:
            states, served = {(fuel[0], fuel[1], 0, 0)}, 0
            for i in range(n):
                nxt = set()
                for f0, f1, t0, t1 in states:
                    if f0 >= demand[i] and t0 <= wait_limit:
                        nxt.add((f0 - demand[i], f1, demand[i], max(0, t1 - t0)))

                    if f1 >= demand[i] and t1 <= wait_limit:
                        nxt.add((f0, f1 - demand[i], max(0, t0 - t1), demand[i]))

                if not nxt:
                    break

                states = nxt
                served += 1

            return served

        mx = check(10**9)
        if mx == 0:
            return -1

        low, high = 0, sum(demand)
        while low <= high:
            mid = (low + high) >> 1
            if check(mid) == mx:
                high = mid - 1
            else:
                low = mid + 1

        return low
