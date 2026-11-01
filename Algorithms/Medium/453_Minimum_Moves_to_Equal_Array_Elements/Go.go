package main

import (
	"slices"
)

func minMoves(nums []int) int {
	result, min_ := 0, slices.Min(nums)
	for _, num := range nums {
		result += num - min_
	}

	return result
}
