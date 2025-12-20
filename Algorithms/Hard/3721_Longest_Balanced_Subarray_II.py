from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        size = 1
        while size < n:
            size <<= 1
        
        min_tree, max_tree, lazy = [0] * (2 * size), [0] * (2 * size), [0] * (2 * size)

        def apply(i: int, d: int) -> None:
            min_tree[i] += d
            max_tree[i] += d
            lazy[i] += d
        
        def push(i: int) -> None:
            if lazy[i]:
                d = lazy[i]
                apply(2*i, d)
                apply(2*i+1, d)
                lazy[i] = 0
        
        def pull(i: int) -> None:
            min_tree[i] = min(min_tree[2*i], min_tree[2*i+1])
            max_tree[i] = max(max_tree[2*i], max_tree[2*i+1])
        
        def range_add(i: int, l: int, r: int, ql: int, qr: int, d: int) -> None:
            if ql > r or qr < l:
                return
            
            if ql <= l and r <= qr:
                apply(i, d)
                return
            
            push(i)
            m = (l + r) // 2
            range_add(2*i, l, m, ql, qr, d)
            range_add(2*i+1, m+1, r, ql, qr, d)
            pull(i)
        
        def find_leftmost_zero(i: int, l: int, r: int, ql: int, qr: int) -> int:
            if ql > r or qr < l:
                return -1
            
            if ql <= l and r <= qr:
                if min_tree[i] > 0 or max_tree[i] < 0:
                    return -1
                
                if l == r:
                    return l if min_tree[i] == 0 else -1
            
            if l == r:
                return -1
            
            push(i)
            m = (l + r) // 2
            left = find_leftmost_zero(2*i, l, m, ql, qr)
            return left if left != -1 else find_leftmost_zero(2*i+1, m+1, r, ql, qr)
        
        result, last = 0, [-1] * (10**5 + 1)
        for r, x in enumerate(nums):
            p = last[x]
            delta = 1 if (x & 1) == 0 else -1
            ql, qr = p + 1, r
            if ql <= qr:
                range_add(1, 0, size - 1, ql, qr, delta)
            
            last[x] = r

            l = find_leftmost_zero(1, 0, size - 1, 0, r)
            if l != -1:
                result = max(result, r-l+1)

        return result
