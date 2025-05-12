class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i in range(len(columnTitle)):
            num = num * 26 + (ord(columnTitle[i]) - ord("A") + 1)
        
        return num
