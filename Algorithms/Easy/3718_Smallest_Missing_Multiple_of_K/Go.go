package main

func missingMultiple(nums []int, k int) int {
	result, seen := k, make(map[int]bool)
	for _, num := range nums {
		seen[num] = true
	}

	for seen[result] {
		result += k
	}

	return result
}
