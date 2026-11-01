class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n+1)
    
    def update(self, idx: int, val: int) -> None:
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx
        
    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx

        return res

class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n, blocks, start, max_so_far = len(nums), [], 0, 0
        for i in range(n):
            max_so_far = max(max_so_far, nums[i])
            if max_so_far == i+1:
                blocks.append((start, i))
                start = i+1
        
        result = 0
        for start, end in blocks:
            if start == end:
                continue
            
            for i in range(start, end+1):
                if locked[i] == 1:
                    result += 1
                    
        if result > k:
            return -1
            
        ft = FenwickTree(n)
        for i in range(n-1, -1, -1):
            result += ft.query(nums[i]-1)
            ft.update(nums[i], 1)
            
        return result
