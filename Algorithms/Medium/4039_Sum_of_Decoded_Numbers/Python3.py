class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9+7
        def power_mod(base: int, exp: int):
            result = 1
            while exp:
                if (exp & 1):
                    result = ((result % mod) * (base % mod)) % mod
                
                base = (base * base) % mod
                exp >>= 1
            
            return result

        result = 0
        for num in nums:
            width, d, digits = num % 10, num // 10, 0
            v = d
            while v:
                digits += 1
                v //= 10
            
            divisor = 1
            for i in range(digits-width):
                divisor *= 10
            
            result = (result + power_mod((d // divisor) % mod, d % divisor)) % mod

        return result
