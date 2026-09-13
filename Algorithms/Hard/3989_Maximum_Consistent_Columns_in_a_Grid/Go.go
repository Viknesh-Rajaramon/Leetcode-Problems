package main

func maxConsistentColumns(grid [][]int, limit int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	for i := range n {
		dp[i] = 1
	}

	for j := 1; j < n; j++ {
		for k := range j {
			is_valid := true
			for i := range m {
				if max(grid[i][j]-grid[i][k], grid[i][k]-grid[i][j]) > limit {
					is_valid = false
					break
				}
			}

			if is_valid {
				dp[j] = max(dp[j], dp[k]+1)
			}
		}
	}

	result := 1
	for _, val := range dp {
		result = max(result, val)
	}

	return result
}
