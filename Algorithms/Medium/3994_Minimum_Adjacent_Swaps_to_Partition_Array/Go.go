package main

func minAdjacentSwaps(nums []int, a int, b int) int {
	result, count_1, count_2, mod := 0, 0, 0, 1000000007
	for _, num := range nums {
		if num < a {
			result = (result + (count_1+count_2)%mod) % mod
		} else if num > b {
			count_2 = (count_2 + 1) % mod
		} else {
			count_1 = (count_1 + 1) % mod
			result = (result + count_2) % mod
		}
	}

	return result
}
