package main

func countCommas(n int) int {
	result, divisor := 0, 1000
	for n >= divisor {
		result += n - divisor + 1
		divisor *= 1000
	}

	return result
}
