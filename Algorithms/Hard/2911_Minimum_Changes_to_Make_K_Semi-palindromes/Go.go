package main

import (
	"math"
	"slices"
)

func minimumChanges(s string, k int) int {
	n := len(s)
	peel := func(i, j, d int) (changes int) {
		for ; j-i > d; i, j = i+d, j-d {
			for t := range d {
				if s[i+t] != s[j-d+t] {
					changes++
				}
			}
		}

		return
	}

	cost := make([][]int, n+1)
	for i := range cost {
		cost[i] = slices.Repeat([]int{math.MaxInt32}, n+1)
	}

	for d := 1; 2*d <= n; d++ {
		for length := 2 * d; length <= n; length += d {
			for i, j := 0, length; j <= n; i, j = i+1, j+1 {
				cost[i][j] = min(cost[i][j], peel(i, j, d))
			}
		}
	}

	best := slices.Repeat([]int{math.MaxInt32}, n+1)
	best[0] = 0
	extend := func(j int) int {
		changes := math.MaxInt32
		for i := range j - 1 {
			changes = min(changes, best[i]+cost[i][j])
		}

		return changes
	}

	for pieces := 1; pieces < k; pieces++ {
		next := slices.Repeat([]int{math.MaxInt32}, n+1)
		for j := 2 * pieces; j <= n-2*(k-pieces); j++ {
			next[j] = extend(j)
		}

		best = next
	}

	return extend(n)
}
