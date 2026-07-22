from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        class SparseTable:
            def __init__(self, data: List[int]):
                self.st = [list(data)]
                i, n = 1, len(self.st[0])
                while 2*i <= n+1:
                    pre = self.st[-1]
                    self.st.append([max(pre[j], pre[j+i]) for j in range(n+1-2*i)])
                    i <<= 1
            
            def query(self, begin: int, end: int) -> int:
                if begin > end:
                    return 0
                
                lg = (end-begin+1).bit_length()-1
                return max(self.st[lg][begin], self.st[lg][end+1-(1<<lg)])
            
        n, count, zero_blocks, left, right, i = len(s), s.count("1"), [], [], [], 0
        while i < n:
            st = i
            while i < n and s[i] == s[st]:
                i += 1
            
            if s[st] == "0":
                zero_blocks.append(i-st)
                left.append(st)
                right.append(i-1)
        
        m = len(zero_blocks)
        if m < 2:
            return [count] * len(queries)
        
        result, tmp_sum = [], [zero_blocks[i] + zero_blocks[i+1] for i in range(m-1)]
        st = SparseTable(tmp_sum)
        for l, r in queries:
            i, j = bisect_left(right, l), bisect_right(left, r)-1
            if i > m-1 or j < 0 or i >= j:
                result.append(count)
                continue

            first, last = right[i]+1-max(left[i], l), min(right[j], r)+1-left[j]
            if i+1 == j:
                result.append(count+first+last)
                continue

            best = max(first+zero_blocks[i+1], zero_blocks[j-1]+last, st.query(i+1, j-2))
            result.append(count+best)

        return result
