package main

func isValid(s string) bool {
	bracket, stack := map[rune]rune{'{': '}', '(': ')', '[': ']'}, make([]rune, 0)
	for _, c := range s {
		if _, ok := bracket[c]; ok {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}

			temp := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if bracket[temp] != c {
				return false
			}
		}
	}

	return len(stack) == 0
}
