package main

import (
	"slices"
)

func minCost(n int, colors string, edges [][]int) int64 {
	g := make([][]int, n)
	for i := range n {
		g[i] = make([]int, 0)
	}

	for _, edge := range edges {
		g[edge[0]] = append(g[edge[0]], edge[1])
		g[edge[1]] = append(g[edge[1]], edge[0])
	}

	type State struct {
		size                    int
		cost_B, cost_R, cost_BR int64
	}

	var dfs func(int, int) State
	dfs = func(u, parent int) State {
		size, cost_B, cost_R, t := 1, int64(0), int64(0), make([]int64, 0)
		for _, v := range g[u] {
			if v == parent {
				continue
			}

			curr := dfs(v, u)
			size += curr.size
			cost_B += curr.cost_B
			cost_R += min(curr.cost_R, curr.cost_B)
			t = append(t, curr.cost_B-min(curr.cost_R, curr.cost_BR))
		}

		slices.Sort(t)
		slices.Reverse(t)
		if colors[u] == 'B' {
			cost_R += int64(size)
		} else {
			cost_B += int64(size)
		}

		cost_BR := int64(0)
		if len(t) > 0 {
			cost_BR = cost_B - t[0]
		}

		return State{size, cost_B, cost_R, cost_BR}
	}

	result := dfs(0, -1)
	return min(result.cost_B, result.cost_R, result.cost_BR)
}
