from functools import lru_cache

class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        @lru_cache(None)
        def solve(x: str, dirs: str, start: int) -> int:
            stop = int(x[0])
            if start > stop:
                return 0

            if not dirs:
                return stop-start+1

            result, y = 0, x[4 if dirs[0] == "D" else 1 : ]
            for d in range(start, stop):
                result += solve("9"*len(y), dirs[1 : ], d)*(10**3 if dirs[0] == "D" else 1)

            if dirs[0] == "D":
                result += solve("9"*len(y), dirs[1 : ], stop)*int(x[1 : 4])

            result += solve(y, dirs[1 : ], stop)
            return result

        return solve(f"{r:016}", directions, 0) - solve(f"{l-1:016}", directions, 0)
