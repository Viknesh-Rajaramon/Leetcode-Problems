package main

func minMoves(classroom []string, energy int) int {
	m, n, k, sr, sc := len(classroom), len(classroom[0]), 0, 0, 0
	dp := make([][]int, m)
	for r := 0; r < m; r++ {
		dp[r] = make([]int, n)
		for c := 0; c < n; c++ {
			if classroom[r][c] == 'S' {
				dp[r][c] = -1
				sr, sc = r, c
			} else if classroom[r][c] == 'L' {
				dp[r][c] = k
				k++
			} else {
				dp[r][c] = -1
			}
		}
	}

	if k == 0 {
		return 0
	}

	total_mask, best := (1<<k)-1, make([][][]int, m)
	for r := 0; r < m; r++ {
		best[r] = make([][]int, n)
		for c := 0; c < n; c++ {
			best[r][c] = make([]int, 1<<k)
			for mask := 0; mask < (1 << k); mask++ {
				best[r][c][mask] = -1
			}
		}
	}

	type State struct {
		r, c, mask, energy, moves int
	}

	best[sr][sc][0] = energy
	dr, dc, queue, i := [4]int{-1, 1, 0, 0}, [4]int{0, 0, -1, 1}, make([]State, 0), 0
	queue = append(queue, State{sr, sc, 0, energy, 0})
	for i < len(queue) {
		curr := queue[i]
		i++

		if curr.energy == 0 {
			continue
		}

		for d := 0; d < 4; d++ {
			nr, nc := curr.r+dr[d], curr.c+dc[d]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || classroom[nr][nc] == 'X' {
				continue
			}

			ne, nmask := curr.energy-1, curr.mask
			if classroom[nr][nc] == 'R' {
				ne = energy
			}

			if classroom[nr][nc] == 'L' {
				nmask |= 1 << dp[nr][nc]
			}

			if nmask == total_mask {
				return curr.moves + 1
			}

			if ne <= best[nr][nc][nmask] {
				continue
			}

			best[nr][nc][nmask] = ne
			queue = append(queue, State{nr, nc, nmask, ne, curr.moves + 1})
		}
	}

	return -1
}
