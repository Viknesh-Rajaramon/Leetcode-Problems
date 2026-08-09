package main

func stoneGameII(piles []int) int {
	n := len(piles)
	dp, suffix := make([][]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n+1)
	}

	suffix[n-1] = piles[n-1]
	for i := n - 2; i >= 0; i-- {
		suffix[i] = suffix[i+1] + piles[i]
	}

	for i := n - 1; i >= 0; i-- {
		for j := 1; j <= n; j++ {
			if i+2*j >= n {
				dp[i][j] = suffix[i]
			} else {
				for k := 1; k <= 2*j; k++ {
					dp[i][j] = max(dp[i][j], suffix[i]-dp[i+k][max(j, k)])
				}
			}
		}
	}

	return dp[0][1]
}
