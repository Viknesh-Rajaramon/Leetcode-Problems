package main

import (
	"math"
)

func maxProductPair(nums []int, target int) []int {
	result, n, best, index := []int{-1, -1}, len(nums), math.MinInt, make(map[int]int)
	for i := range n {
		if _, ok := index[target-nums[i]]; ok {
			j := index[target-nums[i]]
			if nums[i] != nums[j] && nums[i]*nums[j] > best {
				best = nums[i] * nums[j]
				if nums[i] > nums[j] {
					result = []int{i, j}
				} else {
					result = []int{j, i}
				}
			}
		}

		index[nums[i]] = i
	}

	return result
}
