package main

import (
	"math"
)

func minDays(n int) int {
	dp := make([]int, n+1)
	dp[0] = -1
	for i := 1; i <= n; i++ {
		dp[i] = math.MaxInt
	}

	i := 1
	for true {
		f := i * (i + 1) / 2
		if f > n {
			break
		}

		for j := f; j <= n; j++ {
			dp[j] = min(dp[j], dp[j-f]+i+1)
		}

		i++
	}

	return dp[n]
}
