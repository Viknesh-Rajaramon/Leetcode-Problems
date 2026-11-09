package main

func findMismatchedSegments(s1 string, s2 string) [][]string {
	result, n, i := make([][]string, 0), len(s1), 0
	for i < n {
		if s1[i] == s2[i] {
			i++
			continue
		}

		start := i
		for i < n && s1[i] != s2[i] {
			i++
		}

		result = append(result, []string{s1[start:i], s2[start:i]})
	}

	return result
}
