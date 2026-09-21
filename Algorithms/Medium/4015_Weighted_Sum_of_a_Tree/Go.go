package main

func weightedSum(parent []int, nums []int) int64 {
	n := len(parent)
	tree, depth := make([][]int, n), make([]int, n)
	for i := 1; i < n; i++ {
		tree[parent[i]] = append(tree[parent[i]], i)
	}

	var dfs func(u int, d int)
	dfs = func(u int, d int) {
		depth[u] = d
		for _, v := range tree[u] {
			dfs(v, d+1)
		}
	}

	dfs(0, 0)

	height := 0
	for _, d := range depth {
		height = max(height, d)
	}
	height++

	result := int64(0)
	for i := range n {
		result += int64(nums[i] * (height - depth[i]))
	}

	return result
}
