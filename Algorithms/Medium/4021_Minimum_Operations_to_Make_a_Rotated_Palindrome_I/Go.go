package main

import (
	"math"
)

func minOperations(s string) int {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	result, n := math.MaxInt, len(s)
	for k := range n {
		ops := k
		for i := range n / 2 {
			inc := abs(int(s[(k+i)%n]-'a') - int(s[(n+k-1-i)%n]-'a'))
			ops += min(inc, 26-inc)
		}

		result = min(result, ops)
	}

	return result
}
