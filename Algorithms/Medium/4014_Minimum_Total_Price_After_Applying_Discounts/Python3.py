class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        result = 0
        for i in range(min(len(prices), len(discounts))):
            result += prices[i] * (100 - discounts[i]) / 100

        for j in range(i+1, len(prices)):
            result += prices[j]

        return result
