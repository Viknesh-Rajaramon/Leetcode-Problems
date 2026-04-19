from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = sorted(Counter(s).items(), reverse = True, key = lambda x: x[1])
        vowel, cons = False, False
        i = 0
        result = 0
        while i < len(counts):
            if vowel and cons:
                break
            
            if counts[i][0] in ("a", "e", "i", "o", "u"):
                if vowel:
                    i += 1
                    continue
                
                result += counts[i][1]
                vowel = True
            elif not cons:
                result += counts[i][1]
                cons = True

            i += 1

        return result
