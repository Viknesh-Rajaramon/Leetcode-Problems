package main

func cyclicShift(n int, grid [][]int, rowShift []int, colShift []int) [][]int {
	result := make([][]int, n)
	for r := range n {
		result[r] = make([]int, n)
	}

	for r := range n {
		for c := range n {
			nc := (c - rowShift[r] + n) % n
			nr := (r - colShift[nc] + n) % n
			result[nr][nc] = grid[r][c]
		}
	}

	return result
}
