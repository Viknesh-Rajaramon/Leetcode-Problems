package main

func maximumSaleItems(items [][]int, budget int) int {
	n := len(items)
	pre := make([][]int, n)
	for i := 0; i < n; i++ {
		c := 1
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}

			if items[j][0]%items[i][0] == 0 {
				c += 1
			}
		}

		temp := append([]int{}, items[i]...)
		pre[i] = append(temp, c)
	}

	dp := make([]int, budget+1)
	for i := range pre {
		p, cnt := pre[i][1], pre[i][2]
		for b := p; b <= budget; b++ {
			dp[b] = max(dp[b], dp[b-p]+1)
		}

		for b := budget; b >= p; b-- {
			dp[b] = max(dp[b], dp[b-p]+cnt)
		}
	}

	result := 0
	for _, val := range dp {
		if val > result {
			result = val
		}
	}

	return result
}
