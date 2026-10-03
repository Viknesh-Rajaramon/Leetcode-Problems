package main

func longestValidParentheses(s string) int {
	result, stack := 0, []int{-1}
	for i, c := range s {
		if c == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				result = max(result, i-stack[len(stack)-1])
			}
		}
	}

	return result
}
