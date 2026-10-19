package main

func lastVisitedCell(grid [][]byte) []int {
	m, n, r, c := len(grid), len(grid[0]), 0, 0
	for true {
		move := grid[r][c]
		grid[r][c] = 'V'
		nr, nc := r, c
		if move == 'R' {
			nc++
		} else if move == 'L' {
			nc--
		} else if move == 'D' {
			nr++
		} else if move == 'U' {
			nr--
		}

		if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 'V' {
			return []int{r, c}
		}

		r, c = nr, nc
	}

	return []int{r, c}
}
