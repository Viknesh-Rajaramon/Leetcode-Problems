from imports import *

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        letters = Counter(s)
        letters = dict(sorted(letters.items()))
        
        small_str = []
        middle = ""
        for letter, count in letters.items():
            temp = count
            if temp % 2:
                middle = letter
                temp -= 1

            if temp > 0:
                small_str.append(letter * (temp // 2))

        small_str = "".join(small_str)
        return small_str + middle + small_str[::-1]
