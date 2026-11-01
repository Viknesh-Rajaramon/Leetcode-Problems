package main

import (
	"math"
	"math/bits"
)

func minActivationCost(edges [][]int, values []int) int {
	n := len(values)
	graph := make([][][]int, n)
	for _, edge := range edges {
		u, v, c := edge[0], edge[1], edge[2]
		graph[u] = append(graph[u], []int{v, c})
		graph[v] = append(graph[v], []int{u, c})
	}

	add := func(a, b int) int {
		if a == math.MaxInt || b == math.MaxInt || a > math.MaxInt-b {
			return math.MaxInt
		}
		return a + b
	}

	result := math.MaxInt
	var dfs func(int, int) [2]int
	dfs = func(u, parent int) [2]int {
		b, f := bits.OnesCount(uint(values[u]))&1, [2]int{math.MaxInt, math.MaxInt}
		f[b] = 0
		for _, edge := range graph[u] {
			v, c := edge[0], edge[1]
			if v == parent {
				continue
			}

			g := dfs(v, u)
			result = min(result, add(min(add(f[0], g[0]), add(f[1], g[1])), c))
			f[b] = min(f[b], add(g[0], c))
			f[b^1] = min(f[b^1], add(g[1], c))
		}

		return f
	}

	dfs(0, -1)
	if result != math.MaxInt {
		return result
	}

	return -1
}
