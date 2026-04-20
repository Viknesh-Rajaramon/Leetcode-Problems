from typing import List
from math import gcd

class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        class SegmentTree:
            def __init__(self, n: int):
                self.n = n
                self.seg = [0] * (4*n+5)
            
            def build(self, a: List[int], idx: int, low: int, high: int) -> None:
                if low == high:
                    self.seg[idx] = a[low]
                    return
                
                mid = (low+high)//2
                self.build(a, 2*idx, low, mid)
                self.build(a, 2*idx+1, mid+1, high)
                self.seg[idx] = gcd(self.seg[2*idx], self.seg[2*idx+1])
            
            def update(self, idx: int, low: int, high: int, pos: int, val: int) -> None:
                if low == high:
                    self.seg[idx] = val
                    return
                
                mid = (low+high)//2
                if pos <= mid:
                    self.update(2*idx, low, mid, pos, val)
                else:
                    self.update(2*idx+1, mid+1, high, pos, val)
                
                self.seg[idx] = gcd(self.seg[2*idx], self.seg[2*idx+1])
            
            def query(self, idx: int, low: int, high: int, l: int, r: int):
                if r < low or high < l:
                    return 0
                
                if l <= low and high <= r:
                    return self.seg[idx]
                
                mid = (low+high)//2
                left = self.query(2*idx, low, mid, l, r)
                right = self.query(2*idx+1, mid+1, high, l, r)

                return gcd(left, right)
        
        result, n = 0, len(nums)
        arr, st = [nums[i] // p if nums[i] % p == 0 else 0 for i in range(n)], SegmentTree(n)
        st.build(arr, 1, 0, n-1)

        for idx, val in queries:
            nums[idx], arr[idx] = val, val // p if val % p == 0 else 0
            st.update(1, 0, n-1, idx, arr[idx])
            if st.query(1, 0, n-1, 0, n-1) != 1:
                continue
            
            for i in range(n):
                if gcd(st.query(1, 0, n-1, 0, i-1), st.query(1, 0, n-1, i+1, n-1)) == 1:
                    result += 1
                    break

        return result
