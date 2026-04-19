class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        idx = n.find("6")
        if idx == -1:
            return num
        
        return num + 3 * 10**(len(n) - 1 - idx)
