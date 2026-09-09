package main

func countCommas(n int64) int64 {
	result, divisor := int64(0), int64(1000)
	for n >= divisor {
		result += n - divisor + 1
		divisor *= 1000
	}

	return result
}
