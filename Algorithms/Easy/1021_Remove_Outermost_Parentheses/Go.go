package main

func removeOuterParentheses(s string) string {
	result, left, count := make([]byte, 0), 0, 0
	for i, c := range s {
		if c == '(' {
			count++
		} else {
			if count == 1 {
				result = append(result, s[left+1:i]...)
				left = i + 1
				count = 0
			} else {
				count--
			}
		}
	}

	return string(result)
}
