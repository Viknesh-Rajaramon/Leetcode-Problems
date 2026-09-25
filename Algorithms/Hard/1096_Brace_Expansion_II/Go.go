package main

import (
	"sort"
)

func braceExpansionII(expression string) []string {
	op, stack := make([]byte, 0), make([]map[string]bool, 0)
	ope := func() {
		l, r := len(stack)-2, len(stack)-1
		if op[len(op)-1] == '+' {
			for k := range stack[r] {
				stack[l][k] = true
			}
		} else {
			tmp := make(map[string]bool)
			for left := range stack[l] {
				for right := range stack[r] {
					tmp[left+right] = true
				}
			}

			stack[l] = tmp
		}

		op = op[:len(op)-1]
		stack = stack[:len(stack)-1]
	}

	for i := range expression {
		if expression[i] == ',' {
			for len(op) > 0 && op[len(op)-1] == '*' {
				ope()
			}

			op = append(op, '+')
		} else if expression[i] == '{' {
			if i > 0 && (expression[i-1] == '}' || (expression[i-1] >= 'a' && expression[i-1] <= 'z')) {
				op = append(op, '*')
			}

			op = append(op, '{')
		} else if expression[i] == '}' {
			for len(op) > 0 && op[len(op)-1] != '{' {
				ope()
			}

			op = op[:len(op)-1]
		} else {
			if i > 0 && (expression[i-1] == '}' || (expression[i-1] >= 'a' && expression[i-1] <= 'z')) {
				op = append(op, '*')
			}

			stack = append(stack, map[string]bool{string(expression[i]): true})
		}
	}

	for len(op) > 0 {
		ope()
	}

	result := make([]string, 0)
	for k := range stack[0] {
		result = append(result, k)
	}

	sort.Strings(result)
	return result
}
