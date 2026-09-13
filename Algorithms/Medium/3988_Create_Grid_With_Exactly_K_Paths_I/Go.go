package main

import (
	"strings"
)

func createGrid(m int, n int, k int) []string {
	grid, dp, r, c := make([][]string, m), make([][]int, m), min(m, 4), min(n, 4)
	for i := range m {
		grid[i], dp[i] = make([]string, n), make([]int, n)
		for j := range n {
			grid[i][j] = "#"
		}
	}

	var backtrack func(i, j int) bool
	backtrack = func(i, j int) bool {
		if i == r {
			return dp[r-1][c-1] == k
		}

		next_i, next_j := i, j+1
		if next_j == c {
			next_i, next_j = i+1, 0
		}

		grid[i][j] = "."
		if i == 0 && j == 0 {
			dp[i][j] = 1
		} else {
			dp[i][j] = 0
			if i > 0 {
				dp[i][j] += dp[i-1][j]
			}

			if j > 0 {
				dp[i][j] += dp[i][j-1]
			}
		}

		if backtrack(next_i, next_j) {
			return true
		}

		grid[i][j], dp[i][j] = "#", 0
		if !((i == 0 && j == 0) || (i == r-1 && j == c-1)) {
			if backtrack(next_i, next_j) {
				return true
			}
		}

		return false
	}

	if !backtrack(0, 0) {
		return []string{}
	}

	for j := c - 1; j < n; j++ {
		grid[r-1][j] = "."
	}

	for i := r - 1; i < m; i++ {
		grid[i][n-1] = "."
	}

	result := make([]string, m)
	for i, row := range grid {
		result[i] = strings.Join(row, "")
	}

	return result
}
