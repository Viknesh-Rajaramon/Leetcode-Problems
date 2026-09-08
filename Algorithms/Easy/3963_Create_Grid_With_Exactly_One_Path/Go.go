package main

import (
	"strings"
)

func createGrid(m int, n int) []string {
	grid := make([]string, m)
	for r := range m - 1 {
		grid[r] = "." + strings.Repeat("#", n-1)
	}

	grid[m-1] = strings.Repeat(".", n)
	return grid
}
