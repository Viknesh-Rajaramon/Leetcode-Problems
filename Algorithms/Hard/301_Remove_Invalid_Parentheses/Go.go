package main

func removeInvalidParentheses(s string) []string {
	reverse := func(s string) string {
		runes := []rune(s)
		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
			runes[i], runes[j] = runes[j], runes[i]
		}

		return string(runes)
	}

	result := make([]string, 0)
	var helper func(s string, left, right int, open_p, close_p byte)
	helper = func(s string, left, right int, open_p, close_p byte) {
		count := 0
		for right < len(s) {
			if s[right] == open_p {
				count++
			} else if s[right] == close_p {
				count--
			}

			if count < 0 {
				break
			}

			right++
		}

		if count < 0 {
			for left <= right {
				if (s[left] == close_p) && (left == 0 || s[left] != s[left-1]) {
					helper(s[:left]+s[left+1:], left, right, open_p, close_p)
				}

				left++
			}
		} else if count > 0 {
			helper(reverse(s), 0, 0, close_p, open_p)
		} else {
			if open_p == '(' {
				result = append(result, s)
			} else {
				result = append(result, reverse(s))
			}
		}
	}

	helper(s, 0, 0, '(', ')')
	return result
}
