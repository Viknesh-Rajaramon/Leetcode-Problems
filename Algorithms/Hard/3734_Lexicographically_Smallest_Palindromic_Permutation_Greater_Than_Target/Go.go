package main

import (
	"sort"
)

func lexPalindromicPermutation(s string, target string) string {
	freq, odd_count := make(map[byte]int), 0
	for i := 0; i < len(s); i++ {
		freq[s[i]]++
	}

	for _, count := range freq {
		if count%2 != 0 {
			odd_count++
		}
	}

	if odd_count > 1 {
		return ""
	}

	n, sorted_chars := len(s), make([]byte, 0, len(freq))
	for c := range freq {
		sorted_chars = append(sorted_chars, c)
	}

	sort.Slice(sorted_chars, func(i, j int) bool {
		return sorted_chars[i] < sorted_chars[j]
	})

	odd := ""
	if n%2 != 0 {
		for _, c := range sorted_chars {
			if freq[c]%2 != 0 {
				odd = string(c)
				break
			}
		}
	}

	for c := range freq {
		freq[c] /= 2
	}

	result, path := "", make([]byte, 0, n/2)
	var dfs func(i int, tight bool)
	dfs = func(i int, tight bool) {
		if result != "" {
			return
		}

		if i == n/2 {
			path_str, reversed := string(path), make([]byte, len(path))
			for j := range path {
				reversed[len(path)-1-j] = path[j]
			}

			candidate := path_str + string(odd) + string(reversed)
			if !tight || candidate > target {
				result = candidate
			}

			return
		}

		var low byte
		if tight {
			low = target[i]
		}

		for _, c := range sorted_chars {
			if (low == 0 || c >= low) && freq[c] > 0 {
				path = append(path, c)
				freq[c]--
				dfs(i+1, tight && c == low)
				path = path[:len(path)-1]
				freq[c]++
				if result != "" {
					break
				}
			}
		}
	}

	dfs(0, true)
	return result
}
