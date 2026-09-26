package main

import (
	"strings"
)

func evaluate(s string, knowledge [][]string) string {
	result, d, start := &strings.Builder{}, make(map[string]string), -1
	for _, kd := range knowledge {
		d[kd[0]] = kd[1]
	}

	for i, c := range s {
		if c == '(' {
			start = i
		} else if c == ')' {
			if t, ok := d[s[start+1:i]]; ok {
				result.WriteString(t)
			} else {
				result.WriteString("?")
			}

			start = -1
		} else if start < 0 {
			result.WriteRune(c)
		}
	}

	return result.String()
}
