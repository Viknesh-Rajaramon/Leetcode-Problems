package main

func minCost(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dp := make([]map[int]struct{}, n)
	for i := range n {
		dp[i] = make(map[int]struct{})
	}

	dp[0][grid[0][0]] = struct{}{}
	for i := range m {
		for j := range n {
			if i == 0 && j == 0 {
				continue
			}

			curr := make(map[int]struct{})
			if i > 0 {
				for xor := range dp[j] {
					curr[xor^grid[i][j]] = struct{}{}
				}
			}

			if j > 0 {
				for xor := range dp[j-1] {
					curr[xor^grid[i][j]] = struct{}{}
				}
			}

			dp[j] = curr
		}
	}

	result := (1 << 10) - 1
	for val := range dp[n-1] {
		result = min(result, val)
	}

	return result
}
