package main

import (
	"sort"
)

func longestSubarray(nums []int, k int) int {
	n := len(nums)
	first, last, pos, prefix := make([]int, k), make([]int, k), make([][]int, k), 0
	for i := range k {
		first[i] = n + 1
		last[i] = -1
		pos[i] = make([]int, 0)
	}

	first[0], last[0] = 0, 0
	for i := range n {
		val := ((nums[i] % k) + k) % k
		pos[val] = append(pos[val], i)
		prefix = (prefix + val) % k
		last[prefix] = i + 1
		if first[prefix] == n+1 {
			first[prefix] = i + 1
		}
	}

	result := 0
	for i := range k {
		if first[i] != n+1 {
			result = max(result, last[i]-first[i])
		}
	}

	for i := range k {
		if len(pos[i]) == 0 {
			continue
		}

		target := (2 * i) % k
		for j := range k {
			if first[j] == n+1 {
				continue
			}

			r := (j + target) % k
			if last[r] == -1 || last[r]-first[j] <= result {
				continue
			}

			idx := sort.Search(len(pos[i]), func(idx int) bool {
				return pos[i][idx] >= first[j]
			})

			if idx < len(pos[i]) && pos[i][idx] < last[r] {
				result = last[r] - first[j]
			}
		}
	}

	return result
}
