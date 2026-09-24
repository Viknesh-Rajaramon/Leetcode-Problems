package main

func smallestIndex(nums []int) int {
	sum_of_digits := func(num int) int {
		result := 0
		for num > 0 {
			result += num % 10
			num /= 10
		}

		return result
	}

	for i, num := range nums {
		if i == sum_of_digits(num) {
			return i
		}
	}

	return -1
}
