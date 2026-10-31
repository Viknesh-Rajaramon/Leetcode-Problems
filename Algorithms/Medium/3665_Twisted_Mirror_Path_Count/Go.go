package main

func uniquePaths(grid [][]int) int {
	n, mod := len(grid[0]), int(1e9+7)
	dp := make([]int, n)
	dp[0] = 1
	for _, row := range grid {
		prev_dp, prev := dp, 0
		dp = make([]int, n)
		for i, val := range prev_dp {
			if row[i] == 0 {
				dp[i], prev = (prev+val)%mod, (prev+val)%mod
			} else {
				dp[i], prev = prev, val
			}
		}
	}

	return dp[n-1]
}
