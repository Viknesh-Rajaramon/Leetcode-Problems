package main

import (
	"strconv"
)

func goodIntegers(l int64, r int64, k int) int64 {
	type Key struct {
		i       int
		p       int
		tight   bool
		started bool
	}

	solve := func(num int64) int64 {
		s, dp := strconv.FormatInt(num, 10), make(map[Key]int64)
		var dfs func(i int, p int, tight bool, started bool) int64
		dfs = func(i int, p int, tight bool, started bool) int64 {
			if i == len(s) {
				if started {
					return 1
				}

				return 0
			}

			key := Key{i: i, p: p, tight: tight, started: started}
			if _, exists := dp[key]; exists {
				return dp[key]
			}

			result, limit := int64(0), int(s[i]-'0')
			if !tight {
				limit = 9
			}

			for d := 0; d <= limit; d++ {
				if p == -1 && d == 0 {
					result += dfs(i+1, -1, tight && d == limit, false)
				} else if p == -1 || max(p-d, d-p) <= k {
					result += dfs(i+1, d, tight && d == limit, true)
				}
			}

			dp[key] = result
			return result
		}

		return dfs(0, -1, true, false)
	}

	return solve(r) - solve(l-1)
}
