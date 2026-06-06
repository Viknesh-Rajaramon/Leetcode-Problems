package main

func numberOfSpecialChars(word string) int {
	lower := [26]int{}
	upper := [26]int{}
	for i := range lower {
		lower[i] = -1
		upper[i] = -1
	}

	for i, c := range word {
		if c >= 'a' && c <= 'z' {
			lower[c-97] = i
		} else if upper[c-65] == -1 {
			upper[c-65] = i
		}
	}

	result := 0
	for i := range lower {
		if lower[i] != -1 && lower[i] < upper[i] {
			result++
		}
	}

	return result
}
