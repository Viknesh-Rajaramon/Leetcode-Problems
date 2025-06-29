from imports import *

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        def is_prime(num: int) -> bool:
            for i in range(2, int(sqrt(num))+1):
                if num % i == 0:
                    return False

            return True

        for count in counts.values():
            if count > 1 and is_prime(count):
                return True

        return False
