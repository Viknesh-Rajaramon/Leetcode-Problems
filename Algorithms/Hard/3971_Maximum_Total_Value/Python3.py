class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        mod, n = 10**9+7, len(value)
        def is_valid(x: int) -> bool:
            count = 0
            for i in range(n):
                if value[i] >= x:
                    count += ((value[i] - x) // decay[i]) + 1

            return count >= m
        
        low, high = 1, max(value)
        while low <= high:
            mid = (low+high) >> 1
            if is_valid(mid):
                low = mid+1
            else:
                high = mid-1
        
        result, count, threshold = 0, 0, high
        for i in range(n):
            if value[i] < threshold:
                continue
            
            t = ((value[i] - threshold) // decay[i]) + 1
            count += t
            result = (result + (t * (2*value[i] - (t-1)*decay[i]) // 2)) % mod

        return (result + threshold*(m - count)) % mod
