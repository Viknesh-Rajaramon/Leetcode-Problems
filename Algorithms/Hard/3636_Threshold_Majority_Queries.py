from imports import *

class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        new = sorted((len(l), k) for k, l in indices.items())
        n = len(new)
        result = []
        for l, r, threshold in queries:
            x = bisect_left(new, (threshold, -1))
            if x == n:
                result.append(-1)
            else:
                temp = (0, 0)
                for i in range(n - 1, x - 1, -1):
                    if new[i][0] < temp[0]:
                        break
                    
                    idx1 = bisect_right(indices[new[i][1]], r)
                    idx2 = bisect_left(indices[new[i][1]], l)
                    
                    temp = max(temp, (idx1 - idx2, -new[i][1]))
                    if temp[0] > (r - l + 1) // 2:
                        break
                
                if temp[0] >= threshold:
                    result.append(-temp[1])
                else:
                    result.append(-1)

        return result
