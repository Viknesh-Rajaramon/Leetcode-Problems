package main

func largestInteger(n int, s int) int {
	if 9*n < s {
		return -1
	}

	if s == 0 {
		return 0
	}

	result := 0
	for range n {
		d := min(s, 9)
		result = 10*result + d
		s -= d
	}

	return result
}
