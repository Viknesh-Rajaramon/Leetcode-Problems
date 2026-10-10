class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs, k = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))], k1+k2
        total = sum(diffs)
        if k >= total:
            return 0
        
        diffs.sort(reverse = True)
        n, idx, count = len(diffs), 0, 0
        while idx < n:
            curr = diffs[idx]
            while idx < n and diffs[idx] == curr:
                idx += 1
                count += 1
            
            next_value = diffs[idx] if idx < n else 0
            needed = (curr - next_value) * count
            if k < needed:
                remainder, value = k % count, curr - k // count
                result = (count - remainder) * value * value
                result += remainder * (value - 1) * (value - 1)
                for i in range(idx, n):
                    result += diffs[i] * diffs[i]
                
                return result
            
            k -= needed
        
        return 0
