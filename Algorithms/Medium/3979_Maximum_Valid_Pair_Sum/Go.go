package main

import (
	"math"
)

func maxValidPairSum(nums []int, k int) int {
	result, left_max := math.MinInt, math.MinInt
	for r := k; r < len(nums); r++ {
		left_max = max(left_max, nums[r-k])
		result = max(result, left_max+nums[r])
	}

	return result
}
