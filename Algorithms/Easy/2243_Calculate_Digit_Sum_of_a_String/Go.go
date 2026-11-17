package main

import (
	"strconv"
)

func digitSum(s string, k int) string {
	for len(s) > k {
		n, tmp := len(s), ""
		for i := 0; i < n; i += k {
			val := 0
			for j := i; j < min(i+k, n); j++ {
				val += int(s[j] - '0')
			}

			tmp += strconv.Itoa(val)
		}

		s = tmp
	}

	return s
}
