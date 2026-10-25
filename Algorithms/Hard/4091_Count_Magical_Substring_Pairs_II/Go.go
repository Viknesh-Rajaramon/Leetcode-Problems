package main

import (
	"slices"
	"sort"
)

func countMagicalPairs(s string) int64 {
	n := len(s)
	l, r, pos := make([][]int, n), make([][]int, n), make([]int, 26)
	for i := range 26 {
		pos[i] = -1
	}

	for i := range n {
		pos[s[i]-'a'], l[i] = i, make([]int, 27)
		p := make([]int, 0)
		for _, x := range pos {
			if x != -1 {
				p = append(p, x)
			}
		}

		sort.Ints(p)
		slices.Reverse(p)
		for k := range p {
			next := -1
			if k+1 < len(p) {
				next = p[k+1]
			}

			l[i][k+1] = p[k] - next
		}
	}

	for i := range 26 {
		pos[i] = n
	}

	for i := n - 1; i >= 0; i-- {
		pos[s[i]-'a'], r[i] = i, make([]int, 27)
		q := make([]int, 0)
		for _, x := range pos {
			if x != n {
				q = append(q, x)
			}
		}

		sort.Ints(q)
		for k := range q {
			next := n
			if k+1 < len(q) {
				next = q[k+1]
			}

			r[i][k+1] = next - q[k]
		}
	}

	result := int64(0)
	for i := range n - 1 {
		for k := 1; k <= 26; k++ {
			result += int64(l[i][k] * r[i+1][k])
		}
	}

	return result
}
