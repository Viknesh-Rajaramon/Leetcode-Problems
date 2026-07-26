package main

import (
	"math"
)

func maximumProduct(nums []int) int {
	max_1, max_2, max_3 := math.MinInt, math.MinInt, math.MinInt
	min_1, min_2 := math.MaxInt, math.MaxInt
	for _, num := range nums {
		if num > max_1 {
			max_1, max_2, max_3 = num, max_1, max_2
		} else if num > max_2 {
			max_2, max_3 = num, max_2
		} else if num > max_3 {
			max_3 = num
		}

		if num < min_1 {
			min_1, min_2 = num, min_1
		} else if num < min_2 {
			min_2 = num
		}
	}

	return max(max_1*max_2*max_3, min_1*min_2*max_1)
}
