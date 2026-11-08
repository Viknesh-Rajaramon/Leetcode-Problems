package main

func countServers(grid [][]int) int {
	result, m, n := 0, len(grid), len(grid[0])
	for r := range m {
		count, idx := 0, -1
		for c := range n {
			if grid[r][c] == 1 {
				if count == 0 {
					idx = c
				}

				count++
			}
		}

		can_comm := (count != 1)
		if !can_comm {
			for i := range m {
				if i != r && grid[i][idx] == 1 {
					can_comm = true
					break
				}
			}
		}

		if can_comm {
			result += count
		}
	}

	return result
}
