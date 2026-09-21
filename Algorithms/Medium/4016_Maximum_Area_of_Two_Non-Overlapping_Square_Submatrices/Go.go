package main

func maxArea(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	dp, row_max, col_max := make([][]int, m), make([]int, m), make([]int, n)
	for i := range m {
		dp[i] = make([]int, n)
		for j := range n {
			if mat[i][j] == 1 {
				if i == 0 || j == 0 {
					dp[i][j] = 1
				} else {
					dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
				}
			}

			row_max[i] = max(row_max[i], dp[i][j])
			col_max[j] = max(col_max[j], dp[i][j])
		}
	}

	row_suffix := make([]int, m+1)
	for i := m - 1; i >= 0; i-- {
		row_suffix[i] = max(row_suffix[i+1], row_max[i])
	}

	col_suffix := make([]int, n+1)
	for j := n - 1; j >= 0; j-- {
		col_suffix[j] = max(col_suffix[j+1], col_max[j])
	}

	result := 0
	for i := range m {
		for j := range n {
			if dp[i][j] <= result {
				continue
			}

			if i+dp[i][j] < m && row_suffix[i+dp[i][j]] >= dp[i][j] {
				result = dp[i][j]
				continue
			}

			if j+dp[i][j] < n && col_suffix[j+dp[i][j]] >= dp[i][j] {
				result = dp[i][j]
			}
		}
	}

	return result * result
}
