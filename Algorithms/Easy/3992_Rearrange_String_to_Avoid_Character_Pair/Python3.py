class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        result, count_x, count_y = [], 0, 0
        for c in s:
            if c == x:
                count_x += 1
            elif c == y:
                count_y += 1
            else:
                result.append(c)
        
        result += [y] * count_y
        result += [x] * count_x
        return "".join(result)
