package main

import (
	"math"
	"slices"
	"sort"
)

func maxEarnings(meetings [][]int) int64 {
	slices.SortFunc(meetings, func(x, y []int) int {
		return x[1] - y[1]
	})

	result, ends, best := int64(0), []int64{-1}, []int64{math.MinInt64}
	for _, meeting := range meetings {
		start, end, revenue := int64(meeting[0]), int64(meeting[1]), int64(meeting[2])
		pos := sort.Search(len(ends), func(i int) bool {
			return ends[i] > start
		})

		prev := start + best[pos-1]
		if prev > 0 {
			revenue += prev
		}

		result = max(result, revenue)
		if revenue-end > best[len(best)-1] {
			ends = append(ends, end)
			best = append(best, revenue-end)
		}
	}

	return result
}
