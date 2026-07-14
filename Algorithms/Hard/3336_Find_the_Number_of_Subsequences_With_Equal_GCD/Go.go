package main

func subsequencePairCount(nums []int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	mod := 1000000007
	m := 0
	for _, num := range nums {
		m = max(m, num)
	}

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}
	dp[0][0] = 1

	for _, num := range nums {
		new_dp := make([][]int, m+1)
		for i := range new_dp {
			new_dp[i] = make([]int, m+1)
		}

		for i := 0; i <= m; i++ {
			div_1 := gcd(i, num)
			for j := 0; j <= m; j++ {
				if dp[i][j] == 0 {
					continue
				}

				div_2 := gcd(j, num)
				new_dp[i][j] = (new_dp[i][j] + dp[i][j]) % mod
				new_dp[div_1][j] = (new_dp[div_1][j] + dp[i][j]) % mod
				new_dp[i][div_2] = (new_dp[i][div_2] + dp[i][j]) % mod
			}
		}

		dp = new_dp
	}

	result := 0
	for i := 1; i <= m; i++ {
		result = (result + dp[i][i]) % mod
	}

	return result
}
