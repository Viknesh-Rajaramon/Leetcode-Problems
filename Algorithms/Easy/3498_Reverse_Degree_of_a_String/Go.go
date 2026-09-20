package main

func reverseDegree(s string) int {
	result := 0
	for i, c := range s {
		result += (i + 1) * (int('z'-c) + 1)
	}

	return result
}
