package main

import (
	"sort"
)

func countServers(n int, logs [][]int, x int, queries []int) []int {
	sort.Slice(logs, func(i, j int) bool {
		return logs[i][1] < logs[j][1]
	})

	ids := make([]int, len(queries))
	for i := range ids {
		ids[i] = i
	}

	sort.Slice(ids, func(i, j int) bool {
		return queries[ids[i]] < queries[ids[j]]
	})

	result, count, l, r, active := make([]int, len(queries)), make([]int, n+1), 0, 0, 0
	for _, i := range ids {
		for r < len(logs) && logs[r][1] <= queries[i] {
			server := logs[r][0]
			if count[server] == 0 {
				active++
			}

			count[server]++
			r++
		}

		temp := queries[i] - x
		for l < r && logs[l][1] < temp {
			server := logs[l][0]
			count[server]--
			if count[server] == 0 {
				active--
			}

			l++
		}

		result[i] = n - active
	}

	return result
}
