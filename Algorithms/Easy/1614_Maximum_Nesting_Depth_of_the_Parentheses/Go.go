package main

func maxDepth(s string) int {
	result, curr := 0, 0
	for _, c := range s {
		if c == '(' {
			curr++
			result = max(result, curr)
		} else if c == ')' {
			curr--
		}
	}

	return result
}
