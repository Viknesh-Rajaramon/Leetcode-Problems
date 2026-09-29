package main

func hasValidPath(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	if (m+n-1)%2 == 1 {
		return false
	}

	if grid[0][0] != '(' || grid[m-1][n-1] != ')' {
		return false
	}

	type State struct {
		i, j, k int
	}

	visited := make(map[State]bool)
	var dfs func(i, j, k int) bool
	dfs = func(i, j, k int) bool {
		if grid[i][j] == '(' {
			k++
		} else {
			k--
		}

		if k < 0 || k > m-i+n-j-1 {
			return false
		}

		if i == m-1 && j == n-1 {
			return k == 0
		}

		state := State{i, j, k}
		if visited[state] {
			return false
		}

		visited[state] = true
		if i+1 < m && dfs(i+1, j, k) {
			return true
		}

		if j+1 < n && dfs(i, j+1, k) {
			return true
		}

		return false
	}

	return dfs(0, 0, 0)
}
