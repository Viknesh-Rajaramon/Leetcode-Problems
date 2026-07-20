package main

func shiftGrid(grid [][]int, k int) [][]int {
	m, n := len(grid), len(grid[0])
	total := m * n
	k %= total

	shift := func(i, j int) {
		for i < j {
			grid[i/n][i%n], grid[j/n][j%n] = grid[j/n][j%n], grid[i/n][i%n]
			i += 1
			j -= 1
		}
	}

	shift(0, total-1)
	shift(0, k-1)
	shift(k, total-1)

	return grid
}
