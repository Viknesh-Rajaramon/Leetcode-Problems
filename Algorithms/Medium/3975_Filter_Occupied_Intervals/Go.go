package main

import (
	"slices"
)

func filterOccupiedIntervals(occupiedIntervals [][]int, freeStart int, freeEnd int) [][]int {
	slices.SortFunc(occupiedIntervals, func(x []int, y []int) int {
		return x[0] - y[0]
	})

	idx := 0
	for i := 1; i < len(occupiedIntervals); i++ {
		if occupiedIntervals[i][0] <= occupiedIntervals[idx][1]+1 {
			occupiedIntervals[idx][1] = max(occupiedIntervals[idx][1], occupiedIntervals[i][1])
		} else {
			idx++
			occupiedIntervals[idx] = occupiedIntervals[i]
		}
	}

	result := make([][]int, 0)
	for i := range idx + 1 {
		start, end := occupiedIntervals[i][0], occupiedIntervals[i][1]
		if end < freeStart || start > freeEnd {
			result = append(result, []int{start, end})
		}

		if start < freeStart && end >= freeStart {
			result = append(result, []int{start, freeStart - 1})
		}

		if start <= freeEnd && end > freeEnd {
			result = append(result, []int{freeEnd + 1, end})
		}
	}

	return result
}
