from collections import defaultdict

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        index_map = {}
        count_map = defaultdict(int)

        for i in range(len(s)):
            if s[i] in index_map:
                index_map[s[i]][1] = i
            else:
                index_map[s[i]] = [i, i]
            
            count_map[s[i]] += 1
        
        intervals = []
        for i, _ in index_map.values():
            for _, j in index_map.values():
                if i > j:
                    continue

                count = 0
                for c in index_map.keys():
                    if i <= index_map[c][0] <= index_map[c][1] <= j:
                        count += count_map[c]
                    
                if count == j-i+1 and count < len(s):
                    intervals.append([i, j])
                
        intervals.sort(key = lambda x: x[1] - x[0])
        
        result = []
        for i in range(len(intervals)):
            if all(y < intervals[i][0] or intervals[i][1] < x for x, y in result):
                result.append(intervals[i])
        
        return len(result) >= k
