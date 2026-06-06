package main

func numberOfSpecialChars(word string) int {
	letters := make(map[rune]bool)
	for _, c := range word {
		letters[c] = true
	}

	result := 0
	for k, _ := range letters {
		if letters[k] && letters[k-32] {
			result++
		}
	}

	return result
}
