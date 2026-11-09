package main

import (
	"container/heap"
	"slices"
)

type State struct {
	first, second int
}

type PQ []State

func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i, j int) bool {
	if p[i].first != p[j].first {
		return p[i].first < p[j].first
	}

	return p[i].second < p[j].second
}
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(State)) }
func (p *PQ) Pop() interface{} {
	old := *p
	n := len(old)
	item := old[n-1]
	*p = old[:n-1]
	return item
}

func busiestServers(k int, arrival []int, load []int) []int {
	busy, available, num_processed := &PQ{}, &PQ{}, make([]int, k)
	heap.Init(busy)
	heap.Init(available)
	for i := range k {
		heap.Push(available, State{i, 0})
	}

	for i := range len(arrival) {
		for busy.Len() > 0 {
			if (*busy)[0].first <= arrival[i] {
				curr := heap.Pop(busy).(State)
				heap.Push(available, State{i + (k+((curr.second-i)%k))%k, 0})
			} else {
				break
			}
		}

		if available.Len() == 0 {
			continue
		}

		virtual_server := heap.Pop(available).(State)
		next_server := virtual_server.first % k
		num_processed[next_server]++
		heap.Push(busy, State{arrival[i] + load[i], next_server})
	}

	result, max_reqs := make([]int, 0), slices.Max(num_processed)
	for i := range k {
		if num_processed[i] == max_reqs {
			result = append(result, i)
		}
	}

	return result
}
