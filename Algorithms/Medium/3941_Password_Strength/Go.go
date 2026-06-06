package main

func passwordStrength(password string) int {
	result, chars := 0, make(map[rune]int)
	for _, c := range password {
		chars[c]++
	}

	for c, _ := range chars {
		if 'a' <= c && c <= 'z' {
			result += 1
		} else if 'A' <= c && c <= 'Z' {
			result += 2
		} else if '0' <= c && c <= '9' {
			result += 3
		} else {
			result += 5
		}
	}

	return result
}
