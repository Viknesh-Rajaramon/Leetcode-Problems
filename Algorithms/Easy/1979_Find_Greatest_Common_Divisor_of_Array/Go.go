package main

import (
	"slices"
)

func findGCD(nums []int) int {
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}

		return a
	}

	return gcd(slices.Min(nums), slices.Max(nums))
}
