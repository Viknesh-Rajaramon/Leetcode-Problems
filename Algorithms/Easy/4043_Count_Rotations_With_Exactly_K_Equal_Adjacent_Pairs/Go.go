package main

func countRotations(s string, k int) int {
	result := 0
	if s[0] == s[len(s)-1] {
		result++
	}

	for i := range len(s) - 1 {
		if s[i] == s[i+1] {
			result++
		}
	}

	if k == result {
		return len(s) - result
	}

	if k == result-1 {
		return result
	}

	return 0
}
