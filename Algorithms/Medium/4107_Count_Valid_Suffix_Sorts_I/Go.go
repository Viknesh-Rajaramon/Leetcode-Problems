package main

import (
	"slices"
	"sort"
)

func countSuffix(nums []int, target []int) int {
	n, i, ok := len(nums), 0, true
	for i = range n {
		if nums[i] != target[i] {
			ok = false
			break
		}
	}

	if ok {
		i = n - 1
	}

	sort.Sort(sort.Reverse(sort.IntSlice(nums[i:])))
	if !slices.Equal(nums, target) {
		return 0
	}

	result := 1
	for j := i - 1; j >= 0; j-- {
		if target[j] < target[j+1] {
			break
		}

		result++
	}

	return result
}
