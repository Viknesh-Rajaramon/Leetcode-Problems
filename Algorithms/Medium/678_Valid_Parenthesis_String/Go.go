package main

func checkValidString(s string) bool {
	open_count, closed_count, n := 0, 0, len(s)-1
	for i := range n + 1 {
		if s[i] == '(' || s[i] == '*' {
			open_count++
		} else {
			open_count--
		}

		if s[n-i] == ')' || s[n-i] == '*' {
			closed_count++
		} else {
			closed_count--
		}

		if open_count < 0 || closed_count < 0 {
			return false
		}
	}

	return true
}
