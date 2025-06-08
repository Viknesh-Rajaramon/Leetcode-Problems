class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        n = len(num)

        for i in range(n):
            if num[i] != "9":
                break
            
        max_num = num.replace(num[i], "9")

        for i in range(n):
            if num[i] != "0":
                break
            
        min_num = num.replace(num[i], "0")
        return int(max_num) - int(min_num)
