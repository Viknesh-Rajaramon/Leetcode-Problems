class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        F = 28
        L = 28 + (k-1) * 7

        money = k * (F + L) // 2
        for i in range(n % 7):
            money += k + 1 + i
        
        return money
