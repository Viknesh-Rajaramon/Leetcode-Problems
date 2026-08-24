class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        def get(s: str) -> tuple[int, int]:
            nn, qq = 0, 0
            for c in s:
                if c == "?":
                    qq += 1
                else:
                    nn += int(c)
            
            return nn, qq
        
        n0, q0 = get(num[ : n//2])
        n1, q1 = get(num[n//2 : ])
        return (q0+q1) % 2 == 1 or (n0-n1)*2 != (q1-q0)*9
