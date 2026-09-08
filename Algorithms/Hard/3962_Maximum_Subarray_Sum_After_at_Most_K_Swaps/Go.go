package main

import (
	"math"
	"sort"
)

func maxSum(nums []int, k int) int64 {
	result, n := int64(math.MinInt64), len(nums)
	sorted_nums := make([]int, n)
	copy(sorted_nums, nums)
	sort.Ints(sorted_nums)
	initial_others, initial_candidates, split := make([]int, 0), make([]int, 0), max(0, n-k)
	for i := 0; i < split; i++ {
		initial_others = append(initial_others, sorted_nums[i])
	}

	for i := split; i < n; i++ {
		initial_candidates = append(initial_candidates, sorted_nums[i])
	}

	for start := 0; start < n; start++ {
		candidates := append([]int{}, initial_candidates...)
		others := append([]int{}, initial_others...)
		current_sum := int64(0)
		for end := start; end < n; end++ {
			if len(others) > 0 {
				val := nums[end]
				pos := sort.SearchInts(others, nums[end])
				if pos < len(others) && others[pos] == nums[end] {
					others = append(others[:pos], others[pos+1:]...)
				} else {
					last := len(others) - 1
					val = others[last]
					others = others[:last]
				}

				pos = sort.SearchInts(candidates, val)
				candidates = append(candidates, 0)
				copy(candidates[pos+1:], candidates[pos:])
				candidates[pos] = val
			}

			last := len(candidates) - 1
			current_sum += int64(candidates[last])
			candidates = candidates[:last]
			result = max(result, current_sum)
		}
	}

	return result
}
