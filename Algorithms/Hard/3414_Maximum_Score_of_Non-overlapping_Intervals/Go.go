package main

import (
	"sort"
)

func maximumWeight(intervals [][]int) []int {
	type State struct {
		weight  int
		indices []int
	}

	n := len(intervals)
	arr, starts, dp := make([]int, n), make([]int, n), make([][]State, n+1)
	for i := range n {
		arr[i] = i
	}

	sort.Slice(arr, func(i, j int) bool {
		return intervals[arr[i]][0] < intervals[arr[j]][0]
	})

	for i := range n {
		starts[i] = intervals[arr[i]][0]
	}

	for i := range n + 1 {
		dp[i] = make([]State, 5)
	}

	compareSlices := func(a, b []int) bool {
		for i := 0; i < len(a) && i < len(b); i++ {
			if a[i] != b[i] {
				return a[i] < b[i]
			}
		}

		return len(a) < len(b)
	}

	for i := n - 1; i >= 0; i-- {
		row := dp[i]
		idx := arr[i]

		nxt := sort.Search(len(starts), func(k int) bool {
			return starts[k] > intervals[idx][1]
		})

		for j := 1; j < 5; j++ {
			best := dp[i+1][j]
			sub := dp[nxt][j-1]
			sc := sub.weight + intervals[idx][2]
			if sc > best.weight {
				newIndices := make([]int, len(sub.indices)+1)
				copy(newIndices, sub.indices)
				newIndices[len(sub.indices)] = idx
				sort.Ints(newIndices)
				best = State{weight: sc, indices: newIndices}
			} else if sc == best.weight {
				newIndices := make([]int, len(sub.indices)+1)
				copy(newIndices, sub.indices)
				newIndices[len(sub.indices)] = idx
				sort.Ints(newIndices)
				if compareSlices(newIndices, best.indices) {
					best = State{weight: sc, indices: newIndices}
				}
			}

			row[j] = best
		}
	}

	return dp[0][4].indices
}
