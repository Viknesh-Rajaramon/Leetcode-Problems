class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        str_num = str(num)
        for i in range(1, 10):
            if str(i) in str_num and num % i == 0:
                result += str_num.count(str(i))
        
        return result
