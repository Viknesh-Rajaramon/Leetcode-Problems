package main

func smallestSubsequence(s string) string {
	visited, freq := make(map[rune]struct{}), make(map[rune]int, 0)
	for _, c := range s {
		if _, exists := freq[c]; !exists {
			freq[c] = 0
		}

		freq[c]++
	}

	result := make([]rune, 0)
	for _, c := range s {
		freq[c]--
		if _, exists := visited[c]; exists {
			continue
		}

		for len(result) > 0 && result[len(result)-1] > c && freq[result[len(result)-1]] > 0 {
			delete(visited, result[len(result)-1])
			result = result[:len(result)-1]
		}

		result = append(result, c)
		visited[c] = struct{}{}
	}

	return string(result)
}
