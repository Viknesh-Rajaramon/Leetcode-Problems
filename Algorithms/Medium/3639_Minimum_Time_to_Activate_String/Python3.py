from typing import List

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total_substrings = n * (n+1) // 2
        if k > total_substrings:
            return -1
        
        times = [0] * n
        for i in range(n):
            times[order[i]] = i

        def number_of_valid_strings(max_time: int) -> int:
            bad, count = 0, 0
            for i in range(n):
                if times[i] > max_time:
                    count += 1
                elif count > 0:
                    bad += count * (count + 1) // 2
                    count = 0 
            
            if count > 0:
                bad += count * (count + 1) // 2
            
            return total_substrings - bad
        
        low, high = 0, n-1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if number_of_valid_strings(mid) >= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
