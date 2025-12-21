from typing import List

class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort(reverse = True)
        n = len(pizzas)

        i = 0
        days = n // 4
        odd_days = (days % 2) + (days // 2)
        even_days = days - odd_days
        
        max_weight = sum(pizzas[: odd_days]) + sum(pizzas[odd_days+1 : odd_days+1+2*even_days : 2])

        return max_weight
