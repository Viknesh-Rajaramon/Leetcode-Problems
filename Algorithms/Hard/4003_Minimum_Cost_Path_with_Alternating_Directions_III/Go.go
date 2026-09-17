package main

import (
	"container/heap"
	"math"
)

type State struct {
	cost   int64
	i      int
	j      int
	parity int
}

type PQ []State

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i].cost < p[j].cost }
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func minCost(m int, n int, penalty [][]int) int64 {
	moves, dist, pq := [][3]int{{0, 1, 0}, {1, 0, 0}, {0, -1, 1}, {-1, 0, 1}}, make([][][2]int64, m), &PQ{}
	for i := range m {
		dist[i] = make([][2]int64, n)
		for j := range n {
			dist[i][j] = [2]int64{math.MaxInt64, math.MaxInt64}
		}
	}
	dist[0][0][0] = 1

	*pq = append(*pq, State{1, 0, 0, 0})
	heap.Init(pq)
	for pq.Len() > 0 {
		state := heap.Pop(pq).(State)
		if state.cost != dist[state.i][state.j][state.parity] {
			continue
		}

		if state.i == m-1 && state.j == n-1 {
			return state.cost
		}

		new_cost, new_parity := state.cost+int64(penalty[state.i][state.j]), 1-state.parity
		if new_cost < dist[state.i][state.j][new_parity] {
			dist[state.i][state.j][new_parity] = new_cost
			heap.Push(pq, State{new_cost, state.i, state.j, new_parity})
		}

		for _, move := range moves {
			ni, nj := state.i+move[0], state.j+move[1]
			if ni < 0 || ni >= m || nj < 0 || nj >= n {
				continue
			}

			move_cost := int64((ni + 1) * (nj + 1))
			if state.parity != move[2] {
				move_cost += int64(penalty[state.i][state.j])
			}

			new_cost, new_parity := state.cost+move_cost, 1^state.parity
			if new_cost < dist[ni][nj][new_parity] {
				dist[ni][nj][new_parity] = new_cost
				heap.Push(pq, State{new_cost, ni, nj, new_parity})
			}
		}
	}

	return -1
}
