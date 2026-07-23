package main

func uniqueXorTriplets(nums []int) int {
	n := len(nums)
	if n <= 2 {
		return n
	}

	result := 1
	for result <= n {
		result <<= 1
	}

	return result
}
