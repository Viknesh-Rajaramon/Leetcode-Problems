package main

import (
	"sort"
)

func minSelection(availableIntervals [][]int, targetIntervals [][]int) int {
	sort.Slice(targetIntervals, func(i, j int) bool {
		return targetIntervals[i][0] < targetIntervals[j][0]
	})

	sort.Slice(availableIntervals, func(i, j int) bool {
		return availableIntervals[i][0] < availableIntervals[j][0]
	})

	result, n, i, curr, best := 0, len(availableIntervals), 0, 0, 0
	for _, target := range targetIntervals {
		s, e := target[0], target[1]
		for curr < e {
			t := max(curr, s)
			for i < n && availableIntervals[i][0] <= t {
				best = max(best, availableIntervals[i][1])
				i += 1
			}

			if (best < t) || (best == t && t < e) {
				return -1
			}

			curr = best
			result++
		}
	}

	return result
}
