package main

import (
	"strings"
)

func transformStr(s string, strs []string) []bool {
	total_0 := strings.Count(s, "0")
	check := func(t string) bool {
		count_0, count_q := strings.Count(t, "0"), strings.Count(t, "?")
		if total_0 < count_0 || total_0 > count_0+count_q {
			return false
		}

		x := strings.Split(t, "")
		for i, c := range x {
			if count_0 == total_0 {
				break
			}

			if c == "?" {
				x[i] = "0"
				count_0++
			}
		}

		i, j := 0, 0
		for range total_0 {
			for s[i] != '0' {
				i++
			}

			for x[j] != "0" {
				j++
			}

			if i < j {
				return false
			}

			i++
			j++
		}

		return true
	}

	result := make([]bool, len(strs))
	for i, t := range strs {
		result[i] = check(t)
	}

	return result
}
