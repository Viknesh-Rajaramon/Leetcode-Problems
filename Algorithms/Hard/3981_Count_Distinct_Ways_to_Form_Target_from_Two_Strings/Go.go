package main

func interleaveCharacters(word1 string, word2 string, target string) int {
	m, n, mod := len(word1), len(word2), int(1e9+7)
	dp := make([][]int, m+1)
	for i := range m + 1 {
		dp[i] = make([]int, n+1)
	}

	dp[m][n] = 1
	for t := range len(target) {
		new_dp := make([][]int, m+1)
		for i := range m + 1 {
			new_dp[i] = make([]int, n+1)
		}

		for i := range m + 1 {
			acc := dp[i][n]
			for j := range n {
				if word2[j] == target[t] {
					new_dp[i][j] = (new_dp[i][j] + acc) % mod
				}

				acc = (acc + dp[i][j]) % mod
			}
		}

		for j := range n + 1 {
			acc := dp[m][j]
			for i := range m {
				if word1[i] == target[t] {
					new_dp[i][j] = (new_dp[i][j] + acc) % mod
				}

				acc = (acc + dp[i][j]) % mod
			}
		}

		dp = new_dp
	}

	result := 0
	for i := range m {
		for j := range n {
			result = (result + dp[i][j]) % mod
		}
	}

	return result
}
