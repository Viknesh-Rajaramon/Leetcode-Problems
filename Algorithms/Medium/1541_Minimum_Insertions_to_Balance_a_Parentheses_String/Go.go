package main

func minInsertions(s string) int {
	result, n, left_count, i := 0, len(s), 0, 0
	for i < n {
		if s[i] == '(' {
			left_count++
		} else {
			if left_count > 0 {
				left_count--
			} else {
				result++
			}

			if i+1 < n && s[i+1] == ')' {
				i++
			} else {
				result++
			}
		}

		i++
	}

	result += 2 * left_count
	return result
}
