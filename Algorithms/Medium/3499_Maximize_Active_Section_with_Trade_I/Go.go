package main

import (
	"math"
)

func maxActiveSectionsAfterTrade(s string) int {
	count := 0
	for _, c := range s {
		if c == '1' {
			count++
		}
	}

	result, prev, n, i := 0, math.MinInt, len(s), 0
	for i < n {
		start := i
		for i < n && s[i] == s[start] {
			i++
		}

		if s[start] == '0' {
			curr := i - start
			result = max(result, prev+curr)
			prev = curr
		}
	}

	return result + count
}
