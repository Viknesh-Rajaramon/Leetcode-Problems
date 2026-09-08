package main

import (
	"container/heap"
)

type State struct {
	d      int
	streak int
	u      int
}

type PQ []State

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i].d < p[j].d }
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func shortestPath(n int, edges [][]int, labels string, k int) int {
	graph := make([][][2]int, n)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], [2]int{edge[1], edge[2]})
	}

	best_streak, pq := make([]int, n), &PQ{}
	for i := range n {
		best_streak[i] = k + 1
	}

	*pq = append(*pq, State{0, 1, 0})
	heap.Init(pq)
	for pq.Len() > 0 {
		curr := heap.Pop(pq).(State)
		if curr.streak >= best_streak[curr.u] {
			continue
		}

		best_streak[curr.u] = curr.streak
		if curr.u == n-1 {
			return curr.d
		}

		for _, vec := range graph[curr.u] {
			next_streak := 1
			if labels[curr.u] == labels[vec[0]] {
				next_streak += curr.streak
			}

			if next_streak > k || next_streak >= best_streak[vec[0]] {
				continue
			}

			heap.Push(pq, State{curr.d + vec[1], next_streak, vec[0]})
		}
	}

	return -1
}
