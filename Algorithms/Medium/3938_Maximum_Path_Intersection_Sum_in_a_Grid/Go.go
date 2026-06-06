package main

import (
	"math"
)

func maxScore(grid [][]int) int {
	result, m, n := math.MinInt, len(grid), len(grid[0])
	for i := 1; i < m-1; i++ {
		for j := 1; j < n-1; j++ {
			result = max(result, grid[i][j])
		}
	}

	for i := 0; i < m; i++ {
		curr_sum := grid[i][0]
		for j := 1; j < n; j++ {
			curr_sum = max(curr_sum, grid[i][j-1]) + grid[i][j]
			result = max(result, curr_sum)
		}
	}

	for j := 0; j < n; j++ {
		curr_sum := grid[0][j]
		for i := 1; i < m; i++ {
			curr_sum = max(curr_sum, grid[i-1][j]) + grid[i][j]
			result = max(result, curr_sum)
		}
	}

	return result
}
