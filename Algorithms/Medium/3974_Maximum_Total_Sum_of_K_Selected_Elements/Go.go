package main

import (
	"sort"
)

func maxSum(nums []int, k int, mul int) int64 {
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	result, end := int64(0), min(k, mul-1)
	for i := 0; i < end; i++ {
		result += int64(nums[i] * mul)
		mul--
	}

	for i := end; i < k; i++ {
		result += int64(nums[i])
	}

	return result
}
