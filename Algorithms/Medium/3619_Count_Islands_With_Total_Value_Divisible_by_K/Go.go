package main

func countIslands(grid [][]int, k int) int {
	m, n, directions := len(grid), len(grid[0]), [][]int{[]int{1, 0}, []int{-1, 0}, []int{0, 1}, []int{0, -1}}
	var dfs func(int, int) int
	dfs = func(i, j int) int {
		if grid[i][j] == 0 {
			return 0
		}

		sum_ := grid[i][j]
		grid[i][j] = 0
		for _, dir := range directions {
			x, y := i+dir[0], j+dir[1]
			if x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0 {
				continue
			}

			sum_ += dfs(x, y)
		}

		return sum_
	}

	result := 0
	for i := range m {
		for j := range n {
			if grid[i][j] == 0 {
				continue
			}

			if dfs(i, j)%k == 0 {
				result++
			}
		}
	}

	return result
}
