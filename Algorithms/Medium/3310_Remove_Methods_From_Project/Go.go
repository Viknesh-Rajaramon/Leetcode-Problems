package main

func remainingMethods(n int, k int, invocations [][]int) []int {
	edges := make([][]int, n)
	for _, inv := range invocations {
		edges[inv[0]] = append(edges[inv[0]], inv[1])
	}

	suspicious := make([]bool, n)
	suspicious[k] = true

	queue := []int{k}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for _, v := range edges[u] {
			if !suspicious[v] {
				suspicious[v] = true
				queue = append(queue, v)
			}
		}
	}

	for _, inv := range invocations {
		if !suspicious[inv[0]] && suspicious[inv[1]] {
			result := make([]int, n)
			for i := range result {
				result[i] = i
			}

			return result
		}
	}

	result := make([]int, 0)
	for i := 0; i < n; i++ {
		if !suspicious[i] {
			result = append(result, i)
		}
	}

	return result
}
