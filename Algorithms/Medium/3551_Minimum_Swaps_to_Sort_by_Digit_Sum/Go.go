package main

import (
	"sort"
)

func minSwaps(nums []int) int {
	sum_of_digits := func(num int) int {
		result := 0
		for num > 0 {
			result += num % 10
			num /= 10
		}

		return result
	}

	result, n := 0, len(nums)
	sorted_nums := make([]int, n)
	copy(sorted_nums, nums)
	sort.Slice(sorted_nums, func(i, j int) bool {
		a, b := sum_of_digits(sorted_nums[i]), sum_of_digits(sorted_nums[j])
		if a != b {
			return a < b
		}

		return sorted_nums[i] < sorted_nums[j]
	})

	val_idx_map, visited := make(map[int]int), make([]bool, n)
	for idx, val := range sorted_nums {
		val_idx_map[val] = idx
	}

	for i := range n {
		if visited[i] || val_idx_map[nums[i]] == i {
			continue
		}

		cycle_size, j := 0, i
		for !visited[j] {
			visited[j] = true
			j = val_idx_map[nums[j]]
			cycle_size++
		}

		if cycle_size > 1 {
			result += cycle_size - 1
		}
	}

	return result
}
