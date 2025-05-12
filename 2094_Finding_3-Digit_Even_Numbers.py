from imports import *

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counts = Counter(digits)
        print(counts)
        s = set()
        for i in range(1, 10):
            if counts[i] == 0:
                continue
            
            counts[i] -= 1
            for j in range(0, 10):
                if counts[j] == 0:
                    continue
                
                counts[j] -= 1
                for k in range(0, 10, 2):
                    if counts[k] == 0:
                        continue

                    s.add(i*100 + j*10 + k)
                
                counts[j] += 1
            
            counts[i] += 1

        return sorted(list(s))
