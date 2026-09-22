package main

import (
	"math"
	"sort"
)

func elevatorRequests(n int, start int, requests []int) int64 {
	found := false
	for _, r := range requests {
		if r == start {
			found = true
			break
		}
	}

	if !found {
		requests = append(requests, start)
	}

	sort.Ints(requests)
	m := len(requests)
	dp_0, dp_1 := make([][]int64, m), make([][]int64, m)
	for i := range m {
		dp_0[i], dp_1[i] = make([]int64, m), make([]int64, m)
		for j := range m {
			dp_0[i][j], dp_1[i][j] = math.MaxInt64, math.MaxInt64
		}
	}

	start = sort.SearchInts(requests, start)
	dp_0[start][start], dp_1[start][start] = 0, 0
	for l := 1; l < m; l++ {
		rem := int64(m - l)
		for i := range m - l + 1 {
			j := i + l - 1
			if dp_0[i][j] != math.MaxInt64 {
				if i > 0 {
					dp_0[i-1][j] = min(dp_0[i-1][j], dp_0[i][j]+int64(requests[i]-requests[i-1])*rem)
				}

				if j < m-1 {
					dp_1[i][j+1] = min(dp_1[i][j+1], dp_0[i][j]+int64(requests[j+1]-requests[i])*rem)
				}
			}

			if dp_1[i][j] != math.MaxInt64 {
				if i > 0 {
					dp_0[i-1][j] = min(dp_0[i-1][j], dp_1[i][j]+int64(requests[j]-requests[i-1])*rem)
				}

				if j < m-1 {
					dp_1[i][j+1] = min(dp_1[i][j+1], dp_1[i][j]+int64(requests[j+1]-requests[j])*rem)
				}
			}
		}
	}

	return min(dp_0[0][m-1], dp_1[0][m-1])
}
