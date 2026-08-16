package main

func longestSubsequence(nums []int) int {
	all_zero, result := true, 0
	for _, num := range nums {
		result ^= num
		if num != 0 {
			all_zero = false
		}
	}

	if all_zero {
		return 0
	}

	if result == 0 {
		return len(nums) - 1
	}

	return len(nums)
}
