package main

import (
	"slices"
)

func minMoves(nums []int) int {
	result, max_ := 0, slices.Max(nums)
	for _, num := range nums {
		result += max_ - num
	}

	return result
}
