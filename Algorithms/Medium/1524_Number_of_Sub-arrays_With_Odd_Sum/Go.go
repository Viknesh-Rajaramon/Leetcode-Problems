package main

func numOfSubarrays(arr []int) int {
	n, odd_count, curr_sum := len(arr), 0, 0
	for _, num := range arr {
		curr_sum += num
		if curr_sum%2 == 1 {
			odd_count++
		}
	}

	return (odd_count * (n - odd_count + 1)) % (1e9 + 7)
}
