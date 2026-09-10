package main

func maxDigitRange(nums []int) int {
	result, max_digit_range := 0, 0
	for _, num := range nums {
		largest, smallest, x := 0, 10, num
		for x > 0 {
			d := x % 10
			largest, smallest = max(largest, d), min(smallest, d)
			x /= 10
		}

		if largest-smallest > max_digit_range {
			result, max_digit_range = num, largest-smallest
		} else if largest-smallest == max_digit_range {
			result += num
		}
	}

	return result
}
