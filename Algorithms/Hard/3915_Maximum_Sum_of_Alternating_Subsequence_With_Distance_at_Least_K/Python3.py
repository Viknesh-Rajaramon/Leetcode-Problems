from math import inf

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        class FenwickTree:
            def __init__(self, n: int):
                self.n = n
                self.tree = [-inf] * (n+1)

            def put(self, pos: int, val: int) -> None:
                while pos <= self.n:
                    if val > self.tree[pos]:
                        self.tree[pos] = val

                    pos += pos & -pos
            
            def take(self, pos: int) -> int:
                result = -inf
                while pos > 0:
                    if self.tree[pos] >= result:
                        result = self.tree[pos]
                    
                    pos -= pos & -pos
                
                return result
        
        ordered = sorted(set(nums))
        order_rank, width = {v: i+1 for i, v in enumerate(ordered)}, len(ordered)

        low, high = FenwickTree(width), FenwickTree(width)
        up, down = [-inf] * len(nums), [-inf] * len(nums)
        
        result = max(nums)
        for i in range(len(nums)):
            ready = i - k
            if ready >= 0:
                val = nums[ready]
                pos = order_rank[val]
                low.put(pos, max(val, down[ready]))
                high.put(width - pos + 1, max(val, up[ready]))

            curr_val = nums[i]
            curr_pos = order_rank[curr_val]

            prev_l = low.take(curr_pos-1)
            if prev_l != -inf:
                up[i] = prev_l + curr_val
            
            prev_h = high.take(width - curr_pos)
            if prev_h != -inf:
                down[i] = prev_h + curr_val
            
            result = max(result, up[i], down[i])
        
        return result
