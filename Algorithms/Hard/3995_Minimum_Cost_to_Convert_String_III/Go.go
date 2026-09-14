package main

import (
	"math"
)

func minCost(source string, target string, rules [][]string, costs []int) int {
	n := len(source)
	dp := make([]int, n+1)
	for i := range n + 1 {
		dp[i] = -1
	}

	var f func(i int) int
	f = func(i int) int {
		if i == n {
			return 0
		}

		if dp[i] != -1 {
			return dp[i]
		}

		result := math.MaxInt
		if source[i] == target[i] {
			result = f(i + 1)
		}

		for j := range rules {
			x, y := rules[j][0], rules[j][1]
			if i+len(x) > n {
				continue
			}

			valid, wildcard := true, 0
			for k := range x {
				if x[k] != '*' && source[i+k] != x[k] {
					valid = false
					break
				}

				if x[k] == '*' {
					wildcard++
				}

				if y[k] != target[i+k] {
					valid = false
					break
				}
			}

			if !valid {
				continue
			}

			nxt := f(i + len(x))
			if nxt != math.MaxInt {
				result = min(result, costs[j]+wildcard+nxt)
			}
		}

		dp[i] = result
		return result
	}

	result := f(0)
	if result != math.MaxInt {
		return result
	}

	return -1
}
