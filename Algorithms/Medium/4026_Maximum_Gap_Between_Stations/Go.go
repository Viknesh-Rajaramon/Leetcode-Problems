package main

func maximumGap(skill string, station string) int {
	m, n := len(station), len(skill)
	left, right, i := make([]int, n), make([]int, n), 0
	for j := range n {
		for i < m && station[i] != skill[j] {
			i++
		}

		left[j] = i
		i++
	}

	i = m - 1
	for j := n - 1; j >= 0; j-- {
		for i >= 0 && station[i] != skill[j] {
			i--
		}

		right[j] = i
		i--
	}

	result := 0
	for i := range n - 1 {
		result = max(result, right[i+1]-left[i])
	}

	return result
}
