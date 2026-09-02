package main

import (
	"sort"
)

func lexicographicallySmallestArray(nums []int, limit int) []int {
	ordered_nums := make([]int, len(nums))
	copy(ordered_nums, nums)
	sort.Ints(ordered_nums)

	num_to_group, current_group, group_start, prev := make(map[int]int, 0), 0, []int{0}, ordered_nums[0]
	for i, x := range ordered_nums {
		if x-prev > limit {
			current_group++
			group_start = append(group_start, i)
		}

		num_to_group[x], prev = current_group, x
	}

	result := make([]int, 0)
	for _, x := range nums {
		group := num_to_group[x]
		result = append(result, ordered_nums[group_start[group]])
		group_start[group]++
	}

	return result
}
