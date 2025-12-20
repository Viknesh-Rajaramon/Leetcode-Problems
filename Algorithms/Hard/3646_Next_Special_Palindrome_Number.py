from typing import List
from bisect import bisect_right

MAX_HALF_EVEN_LENGTH = 8
SPECIAL_PALINDROMES = [1]

for half_even_length in range(1, MAX_HALF_EVEN_LENGTH + 1):
    half = ["0"] * half_even_length

    def dfs(i: int, included_even_count: List[int], middle_odd_digit: str, middle_odd_rest_count: int) -> None:
        if i == half_even_length:
            if middle_odd_rest_count == 0 and all(included_even_count[even_index] == 0 or included_even_count[even_index] == even_index for even_index in range(1, 5)):
                half_str = "".join(half)

                num = int(half_str + middle_odd_digit + half_str[ : : -1])
                if num <= int(1e16):
                    SPECIAL_PALINDROMES.append(num)

            return
        
        if middle_odd_rest_count:
            half[i] = middle_odd_digit
            dfs(i + 1, included_even_count, middle_odd_digit, middle_odd_rest_count - 1)
        
        for even_index in range(1, 5):
            if included_even_count[even_index] + 1 <= even_index:
                included_even_count[even_index] += 1
                half[i] = str(even_index * 2)
                dfs(i + 1, included_even_count, middle_odd_digit, middle_odd_rest_count)
                included_even_count[even_index] -= 1

    for odd in range(1, 10, 2):
        dfs(0, [0] * 5, str(odd), odd // 2)
    
    dfs(0, [0] * 5, "", 0)

SPECIAL_PALINDROMES.sort()

class Solution:
    def specialPalindrome(self, n: int) -> int:
        return SPECIAL_PALINDROMES[bisect_right(SPECIAL_PALINDROMES, n)]
