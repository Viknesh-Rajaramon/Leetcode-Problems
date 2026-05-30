from typing import List
from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        class SegmentTree:
            def __init__(self, n: int):
                self.max = n
                self.seg = [0] * (n << 2)
            
            def update(self, idx: int, val: int, p: int, l: int, r: int) -> None:
                if l == r:
                    self.seg[p] = val
                    return
                
                mid = (l+r) >> 1
                if idx <= mid:
                    self.update(idx, val, p << 1, l, mid)
                else:
                    self.update(idx, val, p << 1 | 1, mid+1, r)
                
                self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])
            
            def query(self, L: int, R: int, p: int, l: int, r: int) -> int:
                if L <= l and r <= R:
                    return self.seg[p]
                
                mid, res = (l+r) >> 1, 0
                if L <= mid:
                    res = max(res, self.query(L, R, p << 1, l, mid))
                
                if R > mid:
                    res = max(res, self.query(L, R, p << 1 | 1, mid+1, r))
                
                return res
        
        n = min(50000, len(queries) * 3)
        st, sl = SegmentTree(n), SortedList([0, n])
        st.update(n, n, 1, 0, n)

        result = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = min(len(sl)-1, sl.bisect_right(x))
                l, r = sl[idx-1] if idx > 0 else sl[0], sl[idx]
                st.update(x, x-l, 1, 0, n)
                st.update(r, r-x, 1, 0, n)
                sl.add(x)
            else:
                x, sz = q[1], q[2]
                idx = min(len(sl)-1, sl.bisect_right(x))
                pre = sl[idx-1] if idx > 0 else sl[0]
                result.append(max(x-pre, st.query(0, pre, 1, 0, n)) >= sz)

        return result
