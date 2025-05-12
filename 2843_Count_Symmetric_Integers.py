class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            num_str = str(num)
            num_len = len(num_str)
            if num_len % 2:
                continue
            
            mid = num_len // 2
            if sum([int(c) for c in num_str[:mid]]) == sum([int(c) for c in num_str[mid:]]):
                count += 1
        
        return count
