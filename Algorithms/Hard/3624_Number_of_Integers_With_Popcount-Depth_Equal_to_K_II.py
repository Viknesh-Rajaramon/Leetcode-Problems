from imports import *

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        class Fenwick_Tree:
            def __init__(self, n: int):
                self.n = n
                self.tree = [0] * (n+1)

            def update(self, i: int, delta: int) -> None:
                i += 1
                while i <= self.n:
                    self.tree[i] += delta
                    i += i & -i

            def query(self, i: int) -> int:
                i += 1
                result = 0
                while i > 0:
                    result += self.tree[i]
                    i -= i & -i

                return result
            
            def range_query(self, l: int, r: int) -> int:
                return self.query(r) - self.query(l - 1)

        def pop_count_depth(num: int) -> int:
            depth = 0
            while num != 1:
                num = num.bit_count()
                depth += 1

            return depth

        depth_cache = {}
        def get_depth(x: int) -> int:
            if x not in depth_cache:
                depth_cache[x] = pop_count_depth(x)
            
            return depth_cache[x]
        
        n = len(nums)
        max_depth = 6
        depths = [get_depth(num) for num in nums]

        trees = [Fenwick_Tree(n) for _ in range(max_depth + 1)]
        for i, d in enumerate(depths):
            trees[d].update(i, 1)
        
        result = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                count = trees[k].range_query(l, r)
                result.append(count)
            else:
                _, idx, val = q
                old_depth = depths[idx]
                new_depth = get_depth(val)
                if old_depth != new_depth:
                    trees[old_depth].update(idx, -1)
                    trees[new_depth].update(idx, 1)
                    depths[idx] = new_depth
                
                nums[idx] = val

        return result
