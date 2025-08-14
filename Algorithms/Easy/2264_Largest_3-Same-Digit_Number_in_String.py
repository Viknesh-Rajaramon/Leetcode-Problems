class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1
        curr, count = -1, 0
        for c in num:
            if c == curr:
                count += 1
                if count == 3 and int(curr) > result:
                    result = int(curr)
            else:
                curr = c
                count = 1
        
        return str(result) * 3 if result >= 0 else ""
