from bisect import bisect_left, bisect_right, insort

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n+1)
    
    def add(self, i: int, delta: int) -> None:
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def sum(self, i: int) -> int:
        if i < 0:
            return 0
        
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        
        return res
    
    def range_sum(self, l: int, r: int) -> int:
        return self.sum(r) - self.sum(l-1) if r >= l else 0

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        def is_peak(i: int) -> bool:
            return 0 < i < n-1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]

        def f_len(L: int) -> int:
            return (L-2) * (L-1) // 2 if L >= 3 else 0

        bit, peaks, gap_val = Fenwick(n), [], {}
        for i in range(1, n-1):
            if is_peak(i):
                peaks.append(i)
        
        peaks.sort()
        def compute_gap_val(left_peak: int, right_peak: int) -> int:
            return f_len(right_peak - left_peak + 1) if right_peak else 0

        for i in range(len(peaks)-1):
            val = compute_gap_val(peaks[i], peaks[i+1])
            gap_val[peaks[i]] = val
            if val:
                bit.add(peaks[i], val)
        
        if peaks:
            gap_val[peaks[-1]] = 0
        
        def add_peak(p: int) -> None:
            if p in gap_val:
                return
            
            i = bisect_left(peaks, p)
            left = peaks[i-1] if i-1 >= 0 else None
            right = peaks[i] if i < len(peaks) else None
            insort(peaks, p)
            if left is not None:
                new_val = compute_gap_val(left, p)
                prev = gap_val.get(left, 0)
                if new_val != prev:
                    bit.add(left, new_val - prev)
                    gap_val[left] = new_val
            
            new_val_p = compute_gap_val(p, right)
            gap_val[p] = new_val_p
            if new_val_p:
                bit.add(p, new_val_p)

        def remove_peak(p: int) -> None:
            if p not in gap_val:
                return
            
            i = bisect_left(peaks, p)
            left = peaks[i-1] if i-1 >= 0 else None
            right = peaks[i+1] if i+1 < len(peaks) else None
            prev_p = gap_val.get(p, 0)
            if prev_p:
                bit.add(p, -prev_p)
            
            gap_val.pop(p, None)
            del peaks[i]
            if left is not None:
                new_val = compute_gap_val(left, right)
                prev = gap_val.get(left, 0)
                if new_val != prev:
                    bit.add(left, new_val - prev)
                    gap_val[left] = new_val

        def total_subarrays_len_ge_3(L: int) -> int:
            return L*(L+1) // 2 - (2*L - 1) if L >= 3 else 0

        result = []
        for q in queries:
            if q[0] == 1:
                total = total_subarrays_len_ge_3(q[2] - q[1] + 1)
                if total == 0:
                    result.append(0)
                    continue
                
                Lidx = bisect_left(peaks, q[1] + 1)
                Ridx = bisect_right(peaks, q[2] - 1) - 1
                if Lidx > Ridx:
                    result.append(0)
                    continue
                
                internal_sum = bit.range_sum(peaks[Lidx], peaks[Ridx-1]) if Lidx <= Ridx-1 else 0
                no_peak_subarrays = f_len(peaks[Lidx] - q[1]+1) + internal_sum + f_len(q[2] - peaks[Ridx]+1)
                result.append(total - no_peak_subarrays)
            else:
                if nums[q[1]] == q[2]:
                    continue
                
                nums[q[1]] = q[2]
                for j in (q[1]-1, q[1], q[1]+1):
                    if 0 < j < n-1:
                        now = is_peak(j)
                        was = (j in gap_val)
                        if now and not was:
                            add_peak(j)
                        elif not now and was:
                            remove_peak(j)
        
        return result
