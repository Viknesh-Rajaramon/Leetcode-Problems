class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_mirror_number(num: int) -> bool:
            result = []
            while num > 0:
                result.append(num % k)
                num //= k

            return result == result[::-1]
        
        result = 0
        left = 1
        while n > 0:
            right = left * 10
            
            for op in [0, 1]:
                for i in range(left, right):
                    if n == 0:
                        break
                    
                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    
                    if is_k_mirror_number(combined):
                        n -= 1
                        result += combined
                    
            left = right

        return result
