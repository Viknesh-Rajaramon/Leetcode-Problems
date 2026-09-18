package main

import (
	"math"
)

func maxNumOfSubstrings(s string) []string {
	counts, first, last, keys := make(map[byte]int), make(map[byte]int), make(map[byte]int), make([]byte, 0)
	for i := range len(s) {
		c := s[i]
		if _, exists := counts[c]; !exists {
			counts[c] = 0
			first[c] = i
			keys = append(keys, c)
		}

		counts[c]++
		last[c] = i
	}

	result, queue := make([]string, 0), make([][3]int, 0)
	for _, k := range keys {
		queue = append([][3]int{{first[k], last[k], counts[k]}}, queue...)
		l, r, total := math.MaxInt, math.MinInt, 0
		for _, q := range queue {
			total += q[2]
			l = min(l, q[0])
			r = max(r, q[1])
			if total == r-l+1 {
				break
			}
		}

		if total == r-l+1 {
			result = append(result, s[l:r+1])
			queue = make([][3]int, 0)
		}
	}

	return result
}
