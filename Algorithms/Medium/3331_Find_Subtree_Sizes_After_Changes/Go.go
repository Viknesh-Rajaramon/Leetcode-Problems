package main

func findSubtreeSizes(parent []int, s string) []int {
	children := make([][]int, len(s))
	for x := 1; x < len(s); x++ {
		children[parent[x]] = append(children[parent[x]], x)
	}

	result, last := make([]int, len(s)), make(map[byte]int)
	for i := range result {
		result[i] = 1
	}

	var dfs func(int)
	dfs = func(x int) {
		c, above := s[x], -1
		if _, ok := last[c]; ok {
			above = last[c]
		}

		last[c] = x
		for _, child := range children[x] {
			dfs(child)
		}

		last[c] = above
		if x > 0 {
			temp := parent[x]
			if above >= 0 {
				temp = above
			}

			result[temp] += result[x]
		}
	}

	dfs(0)
	return result
}
