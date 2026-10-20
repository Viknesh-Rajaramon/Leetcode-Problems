package main

import (
	"slices"
)

func sortableIntegers(nums []int) int {
	result, n := 0, len(nums)
	check_rotate_sorted := func(nums []int) bool {
		n, downs, down_val, min_val := len(nums), 0, 0, nums[0]
		for i := range n {
			min_val = min(min_val, nums[i])
			if nums[(i+1)%n] < nums[i] {
				downs++
				down_val = nums[(i+1)%n]
			}
		}

		if (downs == 0) || (downs == 1 && down_val == min_val) {
			return true
		}

		return false
	}

	k_partition := func(nums []int, k int) [][]int {
		res := make([][]int, 0)
		for i := 0; i < n; i += k {
			res = append(res, nums[i:i+k])
		}

		return res
	}

	for k := 1; k <= n; k++ {
		if n%k != 0 {
			continue
		}

		partitions := k_partition(nums, k)
		n_p, sortable := len(partitions), true
		for i := range n_p {
			if !check_rotate_sorted(partitions[i]) {
				sortable = false
				break
			}

			if i+1 < n_p && slices.Max(partitions[i]) > slices.Min(partitions[i+1]) {
				sortable = false
				break
			}
		}

		if sortable {
			result += k
		}
	}

	return result
}
