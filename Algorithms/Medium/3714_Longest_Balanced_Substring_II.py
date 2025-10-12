class Solution:
    def longestBalanced(self, s: str) -> int:
        n, result = len(s), 0
        count_a, count_b, count_c, diff = 0, 0, 0, {(0, 0): -1}
        
        for i, c in enumerate(s):
            if c == "a":
                count_a += 1
            elif c == "b":
                count_b += 1
            else:
                count_c += 1
            
            key = (count_a - count_b, count_a - count_c)
            if key in diff:
                result = max(result, i - diff[key])
            else:
                diff[key] = i
        
        ord_a = ord("a")
        for i in range(3):
            if i == 0:
                x, y = ord_a, ord_a+1
            elif i == 1:
                x, y = ord_a+1, ord_a+2
            else:
                x, y = ord_a, ord_a+2

            X, Y, diff = 0, 0, {0: -1}
            for i, c in enumerate(s):
                idx = ord(c)
                if idx == x:
                    X += 1
                elif idx == y:
                    Y += 1
                else:
                    X, Y, diff = 0, 0, {0: i}
                    continue
                
                key = X-Y
                if key in diff:
                    result = max(result, i - diff[key])
                else:
                    diff[key] = i
        
        i = 0
        while i < n:
            j = i
            while i+1 < n and s[i+1] == s[i]:
                i += 1
            
            result = max(result, i-j+1)
            i += 1
        
        return result
