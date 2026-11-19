package main

import (
	"math"
)

func minimizeSum(nums []int) int {
	max_heap := [3]int{math.MinInt, math.MinInt, math.MinInt}
	min_heap := [3]int{math.MaxInt, math.MaxInt, math.MaxInt}
	for _, num := range nums {
		if num < min_heap[0] {
			min_heap[0], min_heap[1], min_heap[2] = num, min_heap[0], min_heap[1]
		} else if num < min_heap[1] {
			min_heap[1], min_heap[2] = num, min_heap[1]
		} else if num < min_heap[2] {
			min_heap[2] = num
		}

		if num > max_heap[0] {
			max_heap[0], max_heap[1], max_heap[2] = num, max_heap[0], max_heap[1]
		} else if num > max_heap[1] {
			max_heap[1], max_heap[2] = num, max_heap[1]
		} else if num > max_heap[2] {
			max_heap[2] = num
		}
	}

	return min(max_heap[2]-min_heap[0], max_heap[1]-min_heap[1], max_heap[0]-min_heap[2])
}
