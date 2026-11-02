package main

import (
	"sort"
)

func minMoves2(nums []int) int {
	sort.Ints(nums)
	result, median := 0, nums[len(nums)/2]
	for _, num := range nums {
		result += max(median-num, num-median)
	}

	return result
}
