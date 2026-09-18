package main

func countValidPrefixes(s string) int {
	result, ones, zeros := 0, 0, 0
	for _, c := range s {
		if c == '1' {
			ones++
		} else {
			zeros++
		}

		if max(zeros-ones, ones-zeros) < 2 {
			result++
		}
	}

	return result
}
