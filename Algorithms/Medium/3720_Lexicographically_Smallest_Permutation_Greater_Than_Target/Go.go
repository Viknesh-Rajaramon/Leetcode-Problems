package main

import (
	"strings"
)

func lexGreaterPermutation(s string, target string) string {
	n, freq := len(s), make([]int, 26)
	for _, c := range s {
		freq[c-'a']++
	}

	result, temp := "", make([]string, 0)
	var dfs func(pos int, found bool) bool
	dfs = func(pos int, found bool) bool {
		if pos == n {
			candidate := strings.Join(temp, "")
			if candidate > target {
				result = candidate
				return true
			}

			return false
		}

		start := 0
		if !found {
			start = int(target[pos] - 'a')
		}

		for i := start; i < 26; i++ {
			if freq[i] > 0 {
				freq[i]--
				temp = append(temp, string(byte('a'+i)))
				if dfs(pos+1, found || i > int(target[pos]-'a')) {
					return true
				}
				temp = temp[:len(temp)-1]
				freq[i]++
			}
		}

		return false
	}

	dfs(0, false)
	return result
}
