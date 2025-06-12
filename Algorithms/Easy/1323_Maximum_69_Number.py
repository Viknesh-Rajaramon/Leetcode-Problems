class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        result = list(n)
        idx = n.find("6")
        if idx == -1:
            return num
        
        result[idx] = "9"
        return int("".join(result))
