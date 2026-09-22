from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        self.tree = [[0] * (k+1) for _ in range(2 << n.bit_length())]
        self.build(nums, 1, 0, n-1)

    def make_leaf(self, o: int, value: int) -> None:
        info, r = [0] * (self.k + 1), value % self.k
        info[r], info[self.k] = 1, r
        self.tree[o] = info

    def merge_pre(self, left: List[int], right: List[int]) -> List[int]:
        pre = [0] * (self.k + 1)
        pre[self.k] = (left[self.k] * right[self.k]) % self.k
        for x in range(self.k):
            pre[x] = left[x]

        for x in range(self.k):
            pre[(left[self.k] * x) % self.k] += right[x]

        return pre

    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.make_leaf(o, nums[l])
            return

        m = (l+r) >> 1
        self.build(nums, o << 1, l, m)
        self.build(nums, (o << 1) | 1, m+1, r)
        self.tree[o] = self.merge_pre(self.tree[o << 1], self.tree[(o << 1) | 1])

    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.make_leaf(o, value)
            return

        m = (l+r) >> 1
        if index <= m:
            self.update(o << 1, l, m, index, value)
        else:
            self.update((o << 1) | 1, m+1, r, index, value)

        self.tree[o] = self.merge_pre(self.tree[o << 1], self.tree[(o << 1) | 1])

    def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
        if L <= l and r <= R:
            return self.tree[o]

        m = (l+r) >> 1
        if R <= m:
            return self.query(o << 1, l, m, L, R)
        
        if L > m:
            return self.query((o << 1) | 1, m+1, r, L, R)

        return self.merge_pre(self.query(o << 1, l, m, L, R), self.query((o << 1) | 1, m+1, r, L, R))

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        result, n, st = [], len(nums), SegmentTree(nums, k)
        for index, value, start, x in queries:
            st.update(1, 0, n-1, index, value)
            result.append(st.query(1, 0, n-1, start, n-1)[x])

        return result
