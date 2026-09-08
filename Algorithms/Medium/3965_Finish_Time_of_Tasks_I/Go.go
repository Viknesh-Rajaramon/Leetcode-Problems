package main

import (
	"math"
)

func finishTime(n int, edges [][]int, baseTime []int) int64 {
	tree := make([][]int, n)
	for _, edge := range edges {
		tree[edge[0]] = append(tree[edge[0]], edge[1])
	}

	var dfs func(u int) int64
	dfs = func(u int) int64 {
		if len(tree[u]) == 0 {
			return int64(baseTime[u])
		}

		earliest, latest := int64(math.MaxInt64), int64(math.MinInt64)
		for _, v := range tree[u] {
			finish := dfs(v)
			earliest, latest = min(earliest, finish), max(latest, finish)
		}

		return latest + (latest - earliest) + int64(baseTime[u])
	}

	return dfs(0)
}
