package main

func minimumGroups(words []string) int {
	duval := func(s string) string {
		n := len(s)
		if n <= 1 {
			return s
		}

		i, j, k := 0, 1, 0
		for i < n && j < n && k < n {
			cik, cjk := s[(i+k)%n], s[(j+k)%n]
			if cik == cjk {
				k++
			} else if cik < cjk {
				j += k + 1
				k = 0
			} else {
				i = max(i+k+1, j)
				j = i + 1
				k = 0
			}
		}

		ans := min(i, j) % n
		return s[ans:] + s[:ans]
	}

	result := make(map[string]struct{})
	for _, w := range words {
		even, odd := make([]byte, 0), make([]byte, 0)
		for i := 0; i < len(w); i += 2 {
			even = append(even, w[i])
			if i+1 < len(w) {
				odd = append(odd, w[i+1])
			}
		}

		result[duval(string(even))+duval(string(odd))] = struct{}{}
	}

	return len(result)
}
