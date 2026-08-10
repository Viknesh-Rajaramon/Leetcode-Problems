package main

import (
	"math"
)

func winnerSquareGame(n int) bool {
	dp := make([]bool, n+1)
	for i := 1; i <= n; i++ {
		for j := int(math.Sqrt(float64(i))); j > 0; j-- {
			if !dp[i-j*j] {
				dp[i] = true
				break
			}
		}
	}

	return dp[n]
}
