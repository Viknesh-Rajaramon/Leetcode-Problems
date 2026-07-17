package main

import (
	"slices"
)

func gcdValues(nums []int, queries []int64) []int {
	mx := slices.Max(nums)
	freq, count := make([]int64, mx+1), make([]int64, mx+1)
	for _, num := range nums {
		freq[num]++
	}

	for g := mx; g > 0; g-- {
		var total int64
		for m := g; m <= mx; m += g {
			total += freq[m]
		}

		pairs := total * (total - 1) / 2
		for m := 2 * g; m <= mx; m += g {
			pairs -= count[m]
		}

		count[g] = pairs
	}

	pref, vals := make([]int64, 0), make([]int, 0)
	var s int64
	for g := 1; g <= mx; g++ {
		if count[g] == 0 {
			continue
		}

		s += count[g]
		pref = append(pref, s)
		vals = append(vals, g)
	}

	result := make([]int, 0)
	for _, q := range queries {
		pos, _ := slices.BinarySearch(pref, q+1)
		result = append(result, vals[pos])
	}

	return result
}
