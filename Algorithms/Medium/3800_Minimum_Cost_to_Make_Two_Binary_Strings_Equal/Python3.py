class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        a, b = 0, 0
        for x, y in zip(s, t):
            if x == y:
                continue
            
            if x == "0" and y == "1":
                a += 1
            else:
                b += 1
        
        pair = min(a, b)
        r = abs(a-b)

        result = pair * min(swapCost, 2*flipCost)
        result += (r // 2) * min(2*flipCost, swapCost + crossCost)
        result += (r % 2) * flipCost
        return result
