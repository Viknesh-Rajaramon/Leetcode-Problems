from imports import *

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr_num = 1
        
        for _ in range(n):
            result.append(curr_num)
            if curr_num * 10 <= n:
                curr_num *= 10
            else:
                while curr_num >= n:
                    curr_num //= 10
                
                curr_num += 1
                
                while curr_num % 10 == 0:
                    curr_num //= 10

        return result
