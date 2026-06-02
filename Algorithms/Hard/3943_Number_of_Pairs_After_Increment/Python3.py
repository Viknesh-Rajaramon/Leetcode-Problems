from collections import Counter

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        class SegmentTree:
            def __init__(self, nums: list[int]):
                self.n = len(nums)
                self.tree = [Counter() for _ in range(self.n << 2)]
                self.lazy = [0] * (self.n << 2)
                self.build(1, 0, self.n-1, nums)
            
            def build(self, node: int, l: int, r: int, nums: list[int]) -> None:
                if l == r:
                    self.tree[node][nums[l]] = 1
                    return
                
                mid = (l+r) >> 1
                self.build(node << 1, l, mid, nums)
                self.build(node << 1 | 1, mid+1, r, nums)
                self.tree[node] = self.tree[node << 1] + self.tree[node << 1 | 1]
            
            def apply(self, node: int, val: int) -> None:
                new_counter = Counter()
                for k, v in self.tree[node].items():
                    new_counter[k+val] = v
                
                self.tree[node] = new_counter
                self.lazy[node] += val

            def update(self, node: int, l: int, r: int, L: int, R: int, val: int) -> None:
                if L <= l and r <= R:
                    self.apply(node, val)
                    return
                
                if self.lazy[node]:
                    self.apply(node << 1, self.lazy[node])
                    self.apply(node << 1 | 1, self.lazy[node])
                    self.lazy[node] = 0

                mid = (l+r) >> 1
                if L <= mid:
                    self.update(node << 1, l, mid, L, R, val)
                
                if R > mid:
                    self.update(node << 1 | 1, mid+1, r, L, R, val)
                
                self.tree[node] = self.tree[node << 1] + self.tree[node << 1 | 1]
            
            def query(self, target: int):
                return self.tree[1][target]
            
        result, st = [], SegmentTree(nums2)
        for q in queries:
            if q[0] == 1:
                st.update(1, 0, st.n-1, q[1], q[2], q[3])
            else:
                result.append(sum(st.query(q[1] - num) for num in nums1))

        return result
