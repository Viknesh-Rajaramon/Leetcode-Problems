package main

import (
	"sort"
)

func countIntersectingIntervals(intervals [][]int) int {
	result, n, i := 0, len(intervals), 0
	starts, ends := make([]int, n), make([]int, n)
	for j := range n {
		starts[j] = intervals[j][0]
		ends[j] = intervals[j][1]
	}

	sort.Ints(starts)
	sort.Ints(ends)

	for j := range n {
		for i < n && ends[i] < starts[j] {
			i++
		}

		result += j - i
	}

	return result
}
