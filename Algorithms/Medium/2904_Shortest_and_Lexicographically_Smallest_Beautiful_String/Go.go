package main

import (
	"strings"
)

func shortestBeautifulSubstring(s string, k int) string {
	if strings.Count(s, "1") < k {
		return ""
	}

	result, left, count := s, 0, 0
	for right, c := range s {
		count += int(c - '0')
		for count > k || s[left] == '0' {
			count -= int(s[left] - '0')
			left++
		}

		if count < k {
			continue
		}

		if right+1-left < len(result) || right+1-left == len(result) && s[left:right+1] < result {
			result = s[left : right+1]
		}
	}

	return result
}
