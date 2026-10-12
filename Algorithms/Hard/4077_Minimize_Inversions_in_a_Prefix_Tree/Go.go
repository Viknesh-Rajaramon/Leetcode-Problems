package main

import (
	"math"
	"math/bits"
	"sort"
)

func minInversions(words []string, target []int) int {
	n := len(words)
	pos := make([]int, n)
	for p, idx := range target {
		pos[idx] = p
	}

	trie, mark := []map[rune]int{map[rune]int{}}, []int{-1}
	for i, w := range words {
		u := 0
		for _, c := range w {
			if _, ok := trie[u][c]; !ok {
				trie[u][c] = len(trie)
				trie = append(trie, map[rune]int{})
				mark = append(mark, -1)
			}

			u = trie[u][c]
		}

		mark[u] = i
	}

	cross := func(A, B []int) int {
		count, j := 0, 0
		for _, x := range A {
			for j < len(B) && B[j] < x {
				j++
			}

			count += j
		}

		return count
	}

	var dfs func(u int) ([]int, int)
	dfs = func(u int) ([]int, int) {
		total, lists := 0, make([][]int, 0)
		for _, v := range trie[u] {
			L, inv := dfs(v)
			total += inv
			lists = append(lists, L)
		}

		c := len(lists)
		if c >= 2 {
			cost := make([][]int, c)
			for i := range c {
				cost[i] = make([]int, c)
			}

			for a := range c {
				for b := a + 1; b < c; b++ {
					x := cross(lists[a], lists[b])
					cost[a][b] = x
					cost[b][a] = len(lists[a])*len(lists[b]) - x
				}
			}

			full, add := 1<<c, make([][]int, 0)
			for j := range c {
				arr := make([]int, full)
				for mask := 1; mask < full; mask++ {
					low := mask & -mask
					arr[mask] = arr[mask^low] + cost[bits.Len(uint(low))-1][j]
				}

				add = append(add, arr)
			}

			dp := make([]int, full)
			for i := range full {
				dp[i] = math.MaxInt
			}
			dp[0] = 0

			for mask := range full {
				if dp[mask] == math.MaxInt {
					continue
				}

				for j := range c {
					bit := 1 << j
					if mask&bit == 0 {
						nd := dp[mask] + add[j][mask]
						if nd < dp[mask|bit] {
							dp[mask|bit] = nd
						}
					}
				}
			}

			total += dp[full-1]
		}

		merged := make([]int, 0)
		for _, L := range lists {
			merged = append(merged, L...)
		}

		sort.Ints(merged)
		if mark[u] >= 0 {
			total += sort.SearchInts(merged, pos[mark[u]])
			merged = append(merged, pos[mark[u]])
			sort.Ints(merged)
		}

		return merged, total
	}

	_, result := dfs(0)
	return result
}
