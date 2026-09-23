package main

import (
	"sort"
)

func elevatorRequests(n int, start int, requests [][]int) int64 {
	abs := func(x int) int {
		if x < 0 {
			return -x
		}

		return x
	}

	sort.Slice(requests, func(i, j int) bool {
		return requests[i][1] < requests[j][1]
	})
	n = len(requests)

	var min_time func(t_i int64, i, j int) int64
	min_time = func(t_i int64, i, j int) int64 {
		t_j := t_i + int64(abs(requests[j][1]-requests[i][1]))
		if abs(j-i) == 1 {
			return t_j
		}

		k := i - 1
		if j > i {
			k = i + 1
		}

		t_k := t_i + int64(abs(requests[k][1]-requests[i][1]))
		if t_k >= int64(requests[k][0]) {
			return min_time(t_k, k, j)
		}

		if t_j+int64(abs(requests[k][1]-requests[j][1])) < int64(requests[k][0]) {
			t_j = int64(requests[k][0] - abs(requests[k][1]-requests[j][1]))
		}

		return min(min_time(int64(requests[k][0]), k, j), min_time(t_j, j, k))
	}

	if n == 1 {
		return int64(max(abs(start-requests[0][1]), requests[0][0]))
	}

	t0 := max(requests[0][0], abs(requests[0][1]-start), requests[n-1][0]-abs(requests[n-1][1]-requests[0][1]))
	t1 := max(requests[n-1][0], abs(requests[n-1][1]-start), requests[0][0]-abs(requests[0][1]-requests[n-1][1]))

	return min(min_time(int64(t0), 0, n-1), min_time(int64(t1), n-1, 0))
}
