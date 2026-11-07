package main

import (
	"container/heap"
)

type State struct {
	first, second, third int
}

type PQ []State

func (p PQ) Len() int { return len(p) }
func (p PQ) Less(i, j int) bool {
	if p[i].first != p[j].first {
		return p[i].first < p[j].first
	}

	if p[i].second != p[j].second {
		return p[i].second < p[j].second
	}

	return p[i].third < p[j].third
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

func assignTasks(servers []int, tasks []int) []int {
	result, busy, idle := make([]int, 0), &PQ{}, &PQ{}
	heap.Init(busy)
	heap.Init(idle)
	for i, w := range servers {
		heap.Push(idle, State{w, i, 0})
	}

	for i, task := range tasks {
		for busy.Len() > 0 && (*busy)[0].first <= i {
			temp := heap.Pop(busy).(State)
			heap.Push(idle, State{temp.second, temp.third, temp.first})
		}

		if idle.Len() > 0 {
			temp := heap.Pop(idle).(State)
			result = append(result, temp.second)
			heap.Push(busy, State{i + task, temp.first, temp.second})
		} else {
			temp := heap.Pop(busy).(State)
			result = append(result, temp.third)
			heap.Push(busy, State{temp.first + task, temp.second, temp.third})
		}
	}

	return result
}
