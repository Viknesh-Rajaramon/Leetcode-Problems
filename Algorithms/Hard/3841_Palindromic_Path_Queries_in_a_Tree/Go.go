package main

import (
	"math/bits"
	"strconv"
	"strings"
)

type FenwickTree struct {
	n    int
	tree []int
}

func NewFenwickTree(n int) *FenwickTree {
	return &FenwickTree{
		n:    n,
		tree: make([]int, n+1),
	}
}

func (ft *FenwickTree) update(i, val int) {
	for i <= ft.n {
		ft.tree[i] ^= val
		i += i & -i
	}
}

func (ft *FenwickTree) query(i int) int {
	result := 0
	for i > 0 {
		result ^= ft.tree[i]
		i -= i & -i
	}

	return result
}

func (ft *FenwickTree) update_range(l, r, val int) {
	ft.update(l, val)
	ft.update(r+1, val)
}

func palindromePath(n int, edges [][]int, s string, queries []string) []bool {
	graph := make([][]int, n)
	for _, edge := range edges {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	LOG, timer := bits.Len(uint(n)), 0
	parent, depth, tin, tout := make([][]int, n), make([]int, n), make([]int, n), make([]int, n)
	for i := range n {
		parent[i] = make([]int, LOG)
	}

	var dfs func(int, int)
	dfs = func(u, par int) {
		timer++
		tin[u], parent[u][0] = timer, par
		for _, v := range graph[u] {
			if v == par {
				continue
			}

			depth[v] = depth[u] + 1
			dfs(v, u)
		}

		tout[u] = timer
	}

	dfs(0, 0)
	for j := 1; j < LOG; j++ {
		for i := range n {
			parent[i][j] = parent[parent[i][j-1]][j-1]
		}
	}

	lca := func(u, v int) int {
		if depth[u] < depth[v] {
			u, v = v, u
		}

		diff := depth[u] - depth[v]
		for i := range LOG {
			if (diff & (1 << i)) != 0 {
				u = parent[u][i]
			}
		}

		if u == v {
			return u
		}

		for i := LOG - 1; i >= 0; i-- {
			if parent[u][i] != parent[v][i] {
				u, v = parent[u][i], parent[v][i]
			}
		}

		return parent[u][0]
	}

	ft, labels := NewFenwickTree(n+1), []byte(s)
	for u, c := range labels {
		ft.update_range(tin[u], tout[u], 1<<(c-'a'))
	}

	result := make([]bool, 0)
	for _, q := range queries {
		parts := strings.Fields(q)
		if parts[0] == "update" {
			u, _ := strconv.Atoi(parts[1])
			c := parts[2][0]
			ft.update_range(tin[u], tout[u], (1<<(labels[u]-'a'))^(1<<(c-'a')))
			labels[u] = c
		} else {
			u, _ := strconv.Atoi(parts[1])
			v, _ := strconv.Atoi(parts[2])
			path_mask := ft.query(tin[u]) ^ ft.query(tin[v]) ^ (1 << (labels[lca(u, v)] - 'a'))
			result = append(result, (path_mask&(path_mask-1)) == 0)
		}
	}

	return result
}
