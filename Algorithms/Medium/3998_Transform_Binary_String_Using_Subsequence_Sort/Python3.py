from typing import List

class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        total_0 = s.count('0')
        def check(t: str) -> bool:
            count_0, count_q = t.count('0'), t.count('?')
            if total_0 < count_0 or total_0 > count_0 + count_q:
                return False

            t = list(t)
            for i, c in enumerate(t):
                if count_0 == total_0:
                    break
                
                if c == '?':
                    t[i] = '0'
                    count_0 += 1

            i, j = 0, 0
            for _ in range(total_0):
                while s[i] != '0':
                    i += 1

                while t[j] != '0':
                    j += 1

                if i < j:
                    return False

                i += 1
                j += 1

            return True

        return [check(t) for t in strs]
