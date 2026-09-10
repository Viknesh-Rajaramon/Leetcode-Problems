class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        result, max_digit_range = 0, 0
        for num in nums:
            largest, smallest, x = 0, 10, num
            while x > 0:
                d = x%10
                largest, smallest = max(largest, d), min(smallest, d)
                x //= 10
            
            if largest-smallest > max_digit_range:
                result, max_digit_range = num, largest-smallest
            elif largest-smallest == max_digit_range:
                result += num

        return result
