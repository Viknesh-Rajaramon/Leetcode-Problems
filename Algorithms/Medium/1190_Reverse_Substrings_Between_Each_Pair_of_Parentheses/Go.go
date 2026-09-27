package main

func reverseParentheses(s string) string {
	result := make([]string, 0)
	result = append(result, "")
	for _, c := range s {
		if c == '(' {
			result = append(result, "")
		} else if c == ')' {
			temp := result[len(result)-1]
			result = result[:len(result)-1]
			runes := []rune(temp)
			for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
				runes[i], runes[j] = runes[j], runes[i]
			}

			result[len(result)-1] += string(runes)
		} else {
			result[len(result)-1] += string(c)
		}
	}

	return result[0]
}
