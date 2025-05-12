# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        mid = 0
        while True:
            mid = (low + high) // 2
            guess_num = guess(mid)

            if guess_num == 0:
                return mid
            elif guess_num == -1:
                high = mid - 1
            elif guess_num == 1:
                low = mid + 1
        
        return 0
