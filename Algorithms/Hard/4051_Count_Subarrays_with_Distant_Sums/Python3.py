class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        result = n*(n+1)//2
        if k == 0:
            return result
        
        a, temp, prefix, k1, k2 = [0] * (n+1), [0] * (n+1), 0, goal-k+1, goal+k-1
        for i, num in enumerate(nums):
            prefix += num
            a[i+1] = prefix
        
        def ff(low: int, high: int):
            nonlocal result
            if low >= high:
                return
            
            mid = (low+high) >> 1
            ff(low, mid)
            ff(mid+1, high)
            p1, p2 = mid+1, mid+1
            for i in range(low, mid+1):
                while p1 <= high and a[p1] < a[i] + k1:
                    p1 += 1

                while p2 <= high and a[p2] <= a[i] + k2:
                    p2 += 1

                result -= p2 - p1

            i, j, p = low, mid+1, low
            while i <= mid and j <= high:
                if a[i] <= a[j]:
                    temp[p] = a[i]
                    i += 1
                else:
                    temp[p] = a[j]
                    j += 1
                
                p += 1

            while i <= mid:
                temp[p] = a[i]
                i += 1
                p += 1

            while j <= high:
                temp[p] = a[j]
                j += 1
                p += 1

            for p in range(low, high+1):
                a[p] = temp[p]

        ff(0, n)
        return result
