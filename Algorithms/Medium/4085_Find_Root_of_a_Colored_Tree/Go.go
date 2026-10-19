package main

func findColoredRoot(edges [][]int, colors string) int {
	n, nxt := len(colors), map[byte]byte{'R': 'B', 'B': 'W', 'W': 'R'}
	in_degree, degree := make([]int, n), make([]int, n)
	for _, edge := range edges {
		degree[edge[0]]++
		degree[edge[1]]++
		if nxt[colors[edge[0]]] == colors[edge[1]] {
			in_degree[edge[1]]++
		} else if nxt[colors[edge[1]]] == colors[edge[0]] {
			in_degree[edge[0]]++
		} else {
			return -1
		}
	}

	result := -1
	for i := range n {
		if in_degree[i] > 1 {
			return -1
		}

		if in_degree[i] == 0 {
			result = i
		}
	}

	if degree[result] <= 2 {
		return result
	}

	return -1
}
