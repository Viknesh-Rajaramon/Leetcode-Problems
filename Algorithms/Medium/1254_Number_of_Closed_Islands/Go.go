package main

func closedIsland(grid [][]int) int {
	result, m, n := 0, len(grid), len(grid[0])
	var dfs func(int, int) bool
	dfs = func(r, c int) bool {
		if r < 0 || r >= m || c < 0 || c >= n {
			return false
		}

		if grid[r][c] == 1 {
			return true
		}

		grid[r][c] = 1
		left, right, up, down := dfs(r, c-1), dfs(r, c+1), dfs(r-1, c), dfs(r+1, c)
		return left && right && up && down
	}

	for r := range m {
		for c := range n {
			if grid[r][c] == 0 && dfs(r, c) {
				result++
			}
		}
	}

	return result
}
