package main

func validSequence(word1 string, word2 string) []int {
	m, n := len(word1), len(word2)
	last, j := make([]int, n), n-1
	for i := m - 1; i >= 0; i-- {
		if word1[i] == word2[j] {
			last[j] = i
			j--
			if j < 0 {
				break
			}
		}
	}

	result, skip, j := make([]int, 0), false, 0
	for i := 0; i < m; i++ {
		if j == n {
			break
		}

		if word1[i] == word2[j] {
			result = append(result, i)
			j++
		} else {
			if !skip && (j == n-1 || last[j+1] > i) {
				skip = true
				result = append(result, i)
				j++
			}
		}
	}

	if j != n {
		return []int{}
	}

	return result
}
