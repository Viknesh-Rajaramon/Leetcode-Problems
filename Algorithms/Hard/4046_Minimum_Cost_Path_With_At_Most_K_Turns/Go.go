package main

import (
	"container/heap"
	"math"
)

type State struct {
	val, r, c, prev_dir, moves int
}

type PQ []State

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i].val < p[j].val }
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func minCost(grid [][]int, k int) int {
	m, n := len(grid), len(grid[0])
	if m == 1 && n == 1 {
		return grid[0][0]
	}

	dirs, pq := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}, &PQ{}
	k++
	dist, dp := make([][]int, m), make([][][]int, m)
	for i := range m {
		dist[i], dp[i] = make([]int, n), make([][]int, n)
		for j := range n {
			dist[i][j], dp[i][j] = math.MaxInt, []int{math.MaxInt, math.MaxInt, math.MaxInt, math.MaxInt}
		}
	}

	*pq = append(*pq, State{grid[0][0], 0, 0, -1, 0})
	heap.Init(pq)
	dist[0][0] = 0
	for pq.Len() > 0 {
		curr := heap.Pop(pq).(State)
		val, r, c, prev_dir, moves := curr.val, curr.r, curr.c, curr.prev_dir, curr.moves
		if r == m-1 && c == n-1 && moves <= k {
			return val
		}

		if prev_dir != -1 {
			if moves >= dp[r][c][prev_dir] {
				continue
			}

			dp[r][c][prev_dir] = moves
		}

		for d := range 4 {
			nr, nc, new_moves := r+dirs[d][0], c+dirs[d][1], moves
			if d != prev_dir {
				new_moves++
			}

			if nr < 0 || nc < 0 || nr >= m || nc >= n || dist[nr][nc] < new_moves || new_moves > k {
				continue
			}

			dist[nr][nc] = new_moves
			heap.Push(pq, State{val + grid[nr][nc], nr, nc, d, new_moves})
		}
	}

	return -1
}
