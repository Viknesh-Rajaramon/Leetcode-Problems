package main

import (
	"math"
)

func firstStableIndex(nums []int, k int) int {
	n := len(nums)
	min_, min_element := make([]int, n), math.MaxInt
	for i := n - 1; i >= 0; i-- {
		min_element = min(min_element, nums[i])
		min_[i] = min_element
	}

	max_ := 0
	for i := 0; i < n; i++ {
		max_ = max(max_, nums[i])
		if max_-min_[i] <= k {
			return i
		}
	}

	return -1
}
