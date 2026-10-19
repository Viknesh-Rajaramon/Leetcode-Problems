package main

import (
	"sort"
)

func targetIndices(nums []int, target int) []int {
	sort.Ints(nums)
	result := make([]int, 0)
	for i, num := range nums {
		if num == target {
			result = append(result, i)
		} else if num > target {
			break
		}
	}

	return result
}
