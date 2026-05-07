class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            
            i = 2
            while i*i <= num:
                if num % i == 0:
                    return False
                
                i += 1
            
            return True

        r = int(str(n)[::-1])
        return sum(num for num in range(min(n, r), max(n, r)+1) if is_prime(num))
