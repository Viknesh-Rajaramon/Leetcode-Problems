class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        mod, count = 10**9+7, r-l+1
        sum_, power = ((l+r) * count // 2) % mod, pow(count, k-1, mod)
        gp_sum = ((pow(10, k, mod)-1) % mod) * pow(9, mod-2, mod) % mod
        return ((sum_ * power) % mod) * gp_sum % mod
