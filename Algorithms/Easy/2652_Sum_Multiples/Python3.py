class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sum_of_nums_divisible_by_k(n: int, k: int) -> int:
            max_ = n // k
            return k * ((max_ * (max_ + 1)) // 2)
        
        return sum_of_nums_divisible_by_k(n, 3) + sum_of_nums_divisible_by_k(n, 5) + sum_of_nums_divisible_by_k(n, 7) - sum_of_nums_divisible_by_k(n, 15) - sum_of_nums_divisible_by_k(n, 21) - sum_of_nums_divisible_by_k(n, 35) + sum_of_nums_divisible_by_k(n, 105)
