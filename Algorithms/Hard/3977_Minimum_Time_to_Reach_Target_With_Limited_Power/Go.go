package main

import (
	"container/heap"
	"math"
)

type State struct {
	t int64
	d int64
	u int
}

type PQ []State

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i].t < p[j].t || (p[i].t == p[j].t && p[i].d < p[j].d) }
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func minTimeMaxPower(n int, edges [][]int, power int, cost []int, source int, target int) []int64 {
	graph, p := make([][][2]int, n), int64(power)
	for _, edge := range edges {
		graph[edge[0]] = append(graph[edge[0]], [2]int{edge[1], edge[2]})
	}

	cost_sp, time, pq := make([]int64, n), make([]int64, n), &PQ{}
	for i := range n {
		cost_sp[i], time[i] = math.MaxInt64, math.MaxInt64
	}

	*pq = append(*pq, State{0, 0, source})
	heap.Init(pq)
	cost_sp[source], time[source] = 0, 0
	for pq.Len() > 0 {
		curr := heap.Pop(pq).(State)
		if curr.d > p {
			continue
		}

		if curr.u == target {
			return []int64{curr.t, p - curr.d}
		}

		if curr.d+int64(cost[curr.u]) > p {
			continue
		}

		for _, vec := range graph[curr.u] {
			if curr.d+int64(cost[curr.u]) < cost_sp[vec[0]] || curr.t+int64(vec[1]) < time[vec[0]] {
				cost_sp[vec[0]], time[vec[0]] = curr.d+int64(cost[curr.u]), curr.t+int64(vec[1])
				heap.Push(pq, State{time[vec[0]], cost_sp[vec[0]], vec[0]})
			}
		}
	}

	return []int64{-1, -1}
}
