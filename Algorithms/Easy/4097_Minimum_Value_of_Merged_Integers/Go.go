package main

import (
	"math"
	"strconv"
)

func minMergedInteger(nums []int) int {
	result := math.MaxInt
	for i := 0; i < len(nums); i += 2 {
		x, _ := strconv.Atoi(strconv.Itoa(nums[i]) + strconv.Itoa(nums[i+1]))
		result = min(result, x)
	}

	return result
}
