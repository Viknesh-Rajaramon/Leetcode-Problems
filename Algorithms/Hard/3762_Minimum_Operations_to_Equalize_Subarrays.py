from typing import List
from itertools import accumulate

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        CNT, SUM, LE, RI = range(4)
        new = lambda: [0, 0, None, None]

        n, pv, p, bad = len(nums), -1, 0, [0]
        for i, v in enumerate(nums):
            v %= k
            p += v != pv
            bad.append(p)
            pv = v

        l = [v // k for v in nums]
        sl = sorted(set(l))
        mp = {v: i for i, v in enumerate(sl)}
        m = len(mp)
        pre = list(accumulate(l, initial=0))

        tr = new()
        trs = [tr]
        
        for v in l:
            tr = tr[:] 
            trs.append(tr)
            
            o = tr
            s, t = 0, m
            i = mp[v]
            
            while True:
                o[CNT] += 1
                o[SUM] += v
                if s + 1 == t:
                    break
                
                mid = s + t >> 1
                if i < mid:
                    o[LE] = o = o[LE][:] if o[LE] else new()
                    t = mid
                else:
                    o[RI] = o = o[RI][:] if o[RI] else new()
                    s = mid

        result = []
        for s, t in queries:
            t += 1
            
            if bad[t] - bad[s + 1]: 
                result.append(-1)
                continue
            
            k_rank = t - s + 1 >> 1    
            a, b = trs[s], trs[t]
            le_cnt = le_sum = 0
            ss, tt = 0, m
                
            while ss + 1 < tt:
                mid = ss + tt >> 1
                c = (b[LE][CNT] if b and b[LE] else 0) - (a[LE][CNT] if a and a[LE] else 0)
                    
                if k_rank <= c:
                    a = a[LE] if a else None
                    b = b[LE] if b else None
                    tt = mid
                else: 
                    le_cnt += c
                    le_sum += (b[LE][SUM] if b and b[LE] else 0) - (a[LE][SUM] if a and a[LE] else 0)
                    k_rank -= c
                    a = a[RI] if a else None
                    b = b[RI] if b else None
                    ss = mid
                
            x = sl[ss]
            ri_cnt = t - s - le_cnt
            ri_sum = pre[t] - pre[s] - le_sum
            result.append(ri_sum - x * ri_cnt + x * le_cnt - le_sum)
                
        return result
