package main

func numDistinct(s string, t string) int {
	m, n := len(s), len(t)
	dp := make([]int, n+1)
	dp[n] = 1
	for i := m - 1; i >= 0; i-- {
		start, end := max(0, n-m+i), min(n-1, i)
		for j := start; j <= end; j++ {
			if s[i] == t[j] {
				dp[j] += dp[j+1]
			}
		}
	}

	return dp[0]
}
