class Solution:
    def concatHex36(self, n: int) -> str:
        if n == 0:
            return "0"
        
        result = ""
        
        base36, n_3 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", n * n * n
        while n_3 > 0:
            result = base36[n_3 % 36] + result
            n_3 //= 36
        
        base16, n_2 = "0123456789ABCDEF", n * n
        while n_2 > 0:
            result = base16[n_2 % 16] + result
            n_2 //= 16
        
        return result
